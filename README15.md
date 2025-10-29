# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6419907e-37ee-3aef-b366-e43c257407ae | -14.60568 | -48.42639 | 2025-10-29 03:55:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 795c9b71-a77b-3d2c-8aa0-0f3018c1b675 | -10.76618 | -47.83311 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d848275d-169c-3d4c-ad43-532e2cfe79ed | -10.86084 | -50.09874 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 023ccb8b-c488-3687-9154-9da37d323e5e | -13.17668 | -48.45032 | 2025-10-29 03:55:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc709cb4-9335-3fcd-b4f4-b4c4686dbd51 | -14.76797 | -43.08098 | 2025-10-29 03:55:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42d2f097-a03d-3a0f-841f-548605bb59d4 | -10.91487 | -48.00338 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 847b3015-1120-3cff-a1bf-ec15a4713452 | -11.94228 | -44.30858 | 2025-10-29 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3f84215-b77e-3282-ae2e-719f931faef9 | -13.74591 | -48.39843 | 2025-10-29 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c298f55-2b4e-3c36-97eb-a88fd69ac44f | -11.97413 | -44.03089 | 2025-10-29 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6721e60e-d93f-3b1e-976e-0b6008806094 | -10.21507 | -45.94735 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| acccb93f-3f47-313e-a04e-1f946d3a4337 | -9.50809 | -46.96198 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 616e60e8-c363-3c85-8e8c-bb94c34ca77d | -12.40012 | -46.6543 | 2025-10-29 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c0d72fa-62ff-39e2-81e9-38ef6cafdd2e | -12.52983 | -47.54411 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf1ac9b5-ab8a-3500-8d13-85037287248b | -9.23034 | -46.35983 | 2025-10-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3899cfc6-ff4e-3dba-9580-80c3c1653dd7 | -9.92822 | -47.67351 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81944995-dfe9-3131-bc8c-da4759dc5b70 | -10.92737 | -43.75932 | 2025-10-29 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25734091-9372-3449-9786-452c10cbaf93 | -13.17611 | -48.45329 | 2025-10-29 03:55:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a8d28cd-6f35-3f98-872c-f6b345a0550a | -11.78592 | -44.16528 | 2025-10-29 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d229d602-4624-341c-8437-92f70f864c1b | -13.31626 | -42.42018 | 2025-10-29 03:55:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 1076210f-b312-3418-aa65-2f321538da26 | -12.14492 | -45.21752 | 2025-10-29 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d940420-fd91-38cd-861c-17ccc05fa11f | -9.89498 | -44.88903 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50cefba6-f3dc-3398-a6f4-43ad9c513158 | -11.11311 | -44.01932 | 2025-10-29 03:55:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 20ad6742-e9aa-37aa-9706-b36077a0805f | -14.27852 | -47.31761 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 80376657-a32c-3200-a22b-3170c3cdcde9 | -11.02664 | -44.64808 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1beb11f2-3e5d-3cd1-b801-52b2ad83b593 | -12.36543 | -50.15738 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e4369d5-6d9e-350b-bf0b-7cc1b2d3c4a8 | -15.10216 | -43.8426 | 2025-10-29 03:55:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 290a09b4-5666-3b4c-a2b4-f2798ad2ed9e | -13.61917 | -46.47062 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6ede127-8fdf-3276-9bf3-aad14e3c48fc | -10.86584 | -50.10416 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b788d6a-1c39-3821-a1f9-4eb46187f992 | -12.9809 | -48.39279 | 2025-10-29 03:55:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66601ecb-eb00-3704-a55a-ced3dfee9a41 | -13.93937 | -48.44241 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 92904523-c822-367c-bcfa-82f311b25ad1 | -13.64325 | -46.51256 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3ce9626e-8a35-31cd-9249-1234be590ca7 | -12.31883 | -46.91677 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 594b180f-2267-3ea8-a8d7-0f220052cbe6 | -9.88348 | -44.87989 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92c66b3b-5566-3bb5-a692-18cae83a604f | -15.11539 | -47.94179 | 2025-10-29 03:55:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b538fc84-5f62-3a4e-a57d-aba846c9c637 | -14.2808 | -47.3055 | 2025-10-29 03:55:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 125b0ad9-2b94-3986-a221-98ff570bbc30 | -8.3839 | -47.74634 | 2025-10-29 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99cd4029-4377-36c8-9159-080f75ea4de4 | -10.4401 | -44.70322 | 2025-10-29 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd3e368d-1df8-3c78-b519-fe1ef3c88203 | -12.35785 | -50.15901 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a46baed6-8f3e-3ca4-bfb3-a72b8ca423be | -11.58987 | -47.95741 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e56dcc28-f563-341c-9b9f-9fa3c550d191 | -10.8568 | -50.12646 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 989f0a95-13e7-3c0d-a5df-233978100ed7 | -13.54165 | -47.13147 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 134264e5-05dc-3944-be1f-3f7286427b5d | -11.97912 | -49.94177 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8685de2f-f29a-386c-ad44-f2d825fe72b9 | -13.15661 | -47.0928 | 2025-10-29 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 357edbfb-ad96-3c2d-b661-1724576c0f92 | -12.00942 | -46.77286 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5798eee9-77ac-34c7-93dd-7f84fc3c03f3 | -11.59043 | -47.95435 | 2025-10-29 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46db9720-54a2-3642-a279-38b648fa60ea | -10.65009 | -48.00423 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4dae2f32-caf7-334b-98bd-19c5b9164e60 | -16.0894 | -46.749 | 2025-10-29 03:55:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72789a65-a616-3cf3-87ef-24473e9951e4 | -13.56141 | -47.32318 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb063c89-3546-34c3-ab5e-d5ee2489f0e7 | -13.34231 | -46.34874 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5634f62-2899-3e37-94af-887c33135d06 | -10.77592 | -44.76121 | 2025-10-29 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc4d780d-bb86-302a-806a-2b278b4b4d03 | -13.36991 | -47.38859 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f40469dd-5425-3a1a-8a4a-09742b12dec8 | -12.09359 | -47.25814 | 2025-10-29 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7524e056-92fd-373f-844b-886a21b3631a | -12.70766 | -46.32026 | 2025-10-29 03:55:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9aa3ad81-fe94-3e87-b1cd-78890dcbbd4f | -9.28738 | -47.02225 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1691a3f5-3853-3942-815a-1cc44246af08 | -10.4667 | -46.39384 | 2025-10-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb236fe6-2a6c-3439-9750-0c919026bdb9 | -9.48758 | -47.33851 | 2025-10-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2eb9dc50-5390-3b8c-bcea-df866bfa7f18 | -10.65326 | -48.01565 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d56e87b-ba62-3bbf-82f2-3da0f67d111b | -12.08449 | -47.99201 | 2025-10-29 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc317efb-44d6-3380-9140-dd7b7cf2a5b7 | -13.65241 | -46.4633 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9969414-00b3-3450-97ef-2e43bdccd2f7 | -10.95617 | -47.61168 | 2025-10-29 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f31f1ea-eab1-3f35-ab4a-ffe720ee8d65 | -13.56534 | -47.33978 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6356140-681a-386a-9b18-e19508af378c | -9.36802 | -43.68293 | 2025-10-29 03:55:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07d536e6-5390-34d5-aabf-748cbc4a7d09 | -10.97796 | -44.76276 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7658d787-4807-3f5e-8c34-25eb857df5ca | -15.55472 | -43.46011 | 2025-10-29 03:55:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c89483b-d5dc-319e-852b-2b37a2d5de1a | -12.36357 | -50.16019 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 525f3c54-72a2-351e-a05b-4d8242201c57 | -13.64054 | -46.50262 | 2025-10-29 03:55:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb466a0f-e332-3289-9b9b-ebffced4ea79 | -13.22072 | -47.07619 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c6c4a18d-56e8-3d92-afe5-32b2816f1d48 | -15.19429 | -47.20708 | 2025-10-29 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d647d5ee-54e1-3271-b712-f0c52a010cb2 | -11.78983 | -44.16598 | 2025-10-29 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c42030ed-2203-3a23-8694-9be487c19172 | -9.62387 | -46.86423 | 2025-10-29 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bfdee6b6-48d5-35b9-920d-c7a2379eaa76 | -13.94841 | -48.47589 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bded2c82-b985-3b74-a41a-9be82b13229e | -14.32214 | -46.52422 | 2025-10-29 03:55:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1de58c8b-65bb-38b7-84b9-dc232cecdea9 | -13.72022 | -42.91413 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 19eb61de-7a77-322c-80ed-81568ba0a769 | -14.29272 | -43.47749 | 2025-10-29 03:55:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bff25df5-d146-3049-8b2b-8b7d6d36d966 | -12.87836 | -48.27912 | 2025-10-29 03:55:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75b3388b-5ee0-374a-96b8-047670664718 | -13.67221 | -47.1945 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 57e6f8a5-4954-381b-a940-17bfb831c101 | -10.6564 | -47.99893 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9e4dbca7-2979-3409-80ff-da9910c60f9d | -10.3557 | -47.56197 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0af333e-c473-37d8-b2c5-dcf8b2b0c1e7 | -13.65502 | -48.44099 | 2025-10-29 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10919c8c-f066-3962-ab49-b88c050e441d | -12.00301 | -46.78181 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b284a23d-ce32-3849-9cf3-5036ad7b693d | -11.03219 | -47.84195 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 176b8dac-f35f-34e8-a2b5-44fac09a838a | -13.55709 | -47.15097 | 2025-10-29 03:55:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 617003dd-1a63-344a-93b9-37554c0d0c6b | -8.69331 | -47.13601 | 2025-10-29 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 598b7447-20a1-3fd7-b985-43f0aecef487 | -13.04782 | -43.82658 | 2025-10-29 03:55:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5e27738-11d1-3fbf-9ea6-51172cc11f30 | -10.76727 | -47.82714 | 2025-10-29 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee3dd146-3ad2-3975-a823-3787fa0d7f62 | -9.09609 | -47.81875 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 620c1af0-4f53-3013-9b49-6bf623df0a61 | -13.5361 | -47.13562 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28c8d5e3-8798-314b-85aa-106f47e43c23 | -11.08569 | -44.84359 | 2025-10-29 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81cc7d2e-a108-3864-8bb8-ef14dd8c911e | -10.4516 | -44.48893 | 2025-10-29 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31a326c1-333b-366e-8d4a-b961a0dd6ed2 | -12.01316 | -46.77859 | 2025-10-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0214147b-69ea-302d-9783-bbf1b83999bf | -13.22163 | -47.0713 | 2025-10-29 03:55:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a24f126f-9e1b-3990-a92d-3c4e38a39ae5 | -10.5176 | -40.32882 | 2025-10-29 03:55:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f3684ee1-12ae-362e-9497-8aa6815c2577 | -13.86664 | -48.49831 | 2025-10-29 03:55:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e72ad61f-ff38-3c95-8fee-33a5246390d5 | -11.03608 | -47.84914 | 2025-10-29 03:55:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96190104-16ee-3e80-971b-3a4aa7971dca | -9.05833 | -45.05085 | 2025-10-29 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02b6ed2a-bef8-3b4f-ad7f-34809b6df68e | -13.64623 | -47.02869 | 2025-10-29 03:55:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2bc7c02c-1f03-3a5e-857a-ea97a4a7d3fa | -15.96918 | -42.98398 | 2025-10-29 03:55:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab7e02fb-3177-3aba-8e84-f7f97dbeb64d | -13.36107 | -47.38385 | 2025-10-29 03:55:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 505dd3e0-58a1-313c-903d-8178261bd929 | -13.58639 | -48.52626 | 2025-10-29 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73803428-b100-3a5d-8aeb-31c1ee2aa347 | -10.86669 | -50.09988 | 2025-10-29 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README16.md)
