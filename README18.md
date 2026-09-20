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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 409f3a0e-1c56-3e48-ab98-1fa7adece6fc | -8.78945 | -48.70652 | 2026-09-20 03:45:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ffaaa5e3-75a5-35c0-98a7-433792ebb8ea | -11.00275 | -46.58464 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a7f152a-01b5-33eb-b4c1-24fcfca4e080 | -7.97072 | -44.06199 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afd9aaff-214a-3635-9673-2cdc38b00aaf | -7.29412 | -46.73828 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e0ca222b-ed0a-3586-a2aa-8728e1a29efc | -7.75643 | -49.19778 | 2026-09-20 03:45:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7bf6782a-320a-32fd-92de-50dedae631ab | -11.87558 | -47.66085 | 2026-09-20 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2672c1d4-43d3-3484-a5f4-a1643a252c2f | -6.29879 | -47.63329 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 53861c1d-a836-341f-956a-19dcc3ed6d55 | -12.34796 | -50.69093 | 2026-09-20 03:45:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cf4ed3e-938c-3b24-aeab-c0c45028ec19 | -13.03043 | -46.91142 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c224114-1893-3fdf-adc3-d1e69225bbe6 | -13.03158 | -46.9085 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61e4d518-0fdc-344d-aa41-fd0e41575261 | -7.09204 | -42.08176 | 2026-09-20 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4c263099-eab2-36e2-b810-91753b99a5ce | -7.52875 | -45.44359 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5edb9a0c-dea9-37ca-b64c-1e97ba86bea2 | -11.2152 | -48.35904 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53a31e98-43de-3564-a8c4-f953e9cac967 | -7.01984 | -45.23989 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 4b03397a-7740-3feb-82d0-6aae0c0cda18 | -11.85718 | -46.87059 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 880aacd6-a286-35dc-8f70-865ee0e75741 | -10.29123 | -50.29553 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0038e54c-5230-38f1-8610-da86d18bd1b1 | -11.32851 | -47.29186 | 2026-09-20 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a83afa41-31c5-3a1b-a584-d91d069f2370 | -8.44072 | -46.84269 | 2026-09-20 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaec9d80-649a-30aa-ada5-e287df6adb69 | -6.56387 | -45.58882 | 2026-09-20 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ae75188-599e-3482-8e3a-c2547d8805b6 | -8.18439 | -40.8181 | 2026-09-20 03:45:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f6e863d1-4240-3f7a-94be-82f48438953c | -12.29493 | -47.11594 | 2026-09-20 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 02b27e87-9f8f-39e5-bf62-431a272f5cc7 | -11.49625 | -47.78267 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d39c340b-75ad-371c-9567-ae84b39b3a52 | -11.83689 | -46.85502 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1590ab3-967d-30da-a186-185a7283ea14 | -9.72529 | -47.26457 | 2026-09-20 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5681a28-8f2a-3c0c-97e8-6ab7a2681a56 | -9.46017 | -45.42899 | 2026-09-20 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cd5db8b-0155-333a-9926-6c765cb6fd85 | -11.04312 | -48.30329 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b2ecae65-c0e5-3268-abfb-59dccba576a0 | -8.79102 | -48.71172 | 2026-09-20 03:45:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8dd82532-11a4-314b-9c6a-b0894557abb3 | -13.00144 | -46.91586 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dee1d582-b37a-3a7a-a754-8934dced4bb1 | -11.03169 | -48.29573 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ca73e92a-617b-3e5c-b8f9-4e3f06b5bc72 | -9.36435 | -40.30769 | 2026-09-20 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 184e2f18-e5bd-348d-ae51-31ad0a3cdb32 | -6.20405 | -47.52702 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc91bea5-d151-33df-a860-ed027898ad1b | -10.32222 | -48.0028 | 2026-09-20 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1537156b-58c0-3d58-9016-ac6169b257a4 | -11.03596 | -48.31819 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5193c69-e51a-300d-9e95-8a9f29e074e3 | -12.13722 | -47.02548 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd3b8e79-451e-31e8-945e-f8476e2d4a45 | -11.32355 | -47.28635 | 2026-09-20 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db40ba5f-f765-37ca-83a3-31bf8a80ef31 | -12.53225 | -50.03199 | 2026-09-20 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1121e8d4-ac15-340c-9a5d-b060c75f60e2 | -7.44402 | -44.73966 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20c36b7b-cbc7-38ee-b9a4-87738e377c10 | -7.58853 | -46.30551 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d939187-16d0-35d1-b848-f90047a1f8c2 | -9.26262 | -46.20732 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c92c92a3-0b56-300c-9d26-8e6ae23064ca | -6.30657 | -47.62694 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3dabd806-403c-35a5-a868-08e0509ab1c8 | -12.37468 | -45.80577 | 2026-09-20 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d87e595-5b03-3e8f-9475-dc8a22a002f3 | -10.66649 | -47.43703 | 2026-09-20 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50319e44-e2ac-3bcb-8a04-3c6473090a43 | -6.60698 | -43.75475 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bace9e7b-7d16-32a3-932f-d1ca0cfe03c1 | -10.32427 | -48.00106 | 2026-09-20 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae03ab06-9cc0-3f24-98af-2b495c53315f | -7.45053 | -44.73375 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 10aa1a7d-fa80-3a15-a5f6-9d0e4c5448e0 | -12.76341 | -46.12602 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7216e696-f4f4-33c5-bc88-a46db32c3a60 | -7.88383 | -44.85136 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7cc9c9c-9c56-32ab-ab2c-d61d8c99af63 | -7.18184 | -47.89429 | 2026-09-20 03:45:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d71f76d-ad4a-3ff0-8389-92ea9c7c983c | -11.03691 | -48.30195 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d30f064b-ed94-37c7-b442-145ebe0e37fd | -7.97228 | -44.05328 | 2026-09-20 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4d44a3d-1cbd-37f4-be83-6b197199b6bc | -10.39044 | -48.90145 | 2026-09-20 03:45:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f801ea9b-87d8-3e87-8c9e-2e13fc654661 | -8.43009 | -45.86341 | 2026-09-20 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44319c08-1b4f-3098-9a08-f4322d1dddfc | -12.13488 | -47.03762 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ecca1761-bd41-3573-8dde-edfdc1ea1a5f | -10.49353 | -46.26609 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4ea677f4-52b8-30ee-a4a4-1640dfc244e9 | -11.66164 | -43.43425 | 2026-09-20 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d2b1ced4-3537-3fd1-add2-658dfc7491ad | -10.30379 | -50.25034 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 8d8c5d73-9651-3038-b63b-6d0bf4dd3d28 | -13.03018 | -46.91575 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 53c22319-1c91-3b34-bcd3-854c3be783a2 | -9.96104 | -46.54369 | 2026-09-20 03:45:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69f6b0c1-c7e5-3a8f-b054-97fc43e9e54e | -12.13191 | -47.03584 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 29bef7c1-6335-37db-b9ed-e35545302321 | -11.09091 | -48.29095 | 2026-09-20 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 06d03399-4910-3d5e-823c-caec53cb3687 | -11.87766 | -48.99966 | 2026-09-20 03:45:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e7d4486d-40b8-3e34-b2fd-abb07ae9134b | -7.43749 | -44.7457 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 631ec033-35aa-3d63-b8cb-69b41d6a3272 | -7.7949 | -44.91951 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a722441d-197b-3316-adee-540f40f653fe | -6.29012 | -47.60704 | 2026-09-20 03:45:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 417f8c67-9b8c-3659-b075-9f471b159a7e | -7.86191 | -44.85172 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8d5b174-0251-3d0e-91c6-c955b7eb6b47 | -10.46658 | -45.08752 | 2026-09-20 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de7d8d4c-f5ea-37ce-8971-c52217c9e78e | -7.59442 | -46.30629 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69bc7131-5557-3aa0-87f7-209ad24ee99e | -7.55845 | -45.43718 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 349c40b7-d8c1-3dd8-8d22-04f670f690ea | -11.44825 | -45.39903 | 2026-09-20 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6775637b-5412-3065-aafe-b45fc4d52917 | -6.68552 | -43.6287 | 2026-09-20 03:45:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e33dd9b-7500-37b9-a82c-3e3313104f24 | -11.00895 | -48.31193 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3f36e7d-197f-3dbb-8fdd-d984279e3df4 | -9.73047 | -46.08485 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a40f228-03ae-382d-a2b5-b19e5aa84976 | -7.77305 | -44.83521 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26f9f4be-4b13-3fe9-acb8-f672057cbb66 | -11.23755 | -48.38879 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e994c087-58e6-319b-90d5-745696f2d5db | -12.75407 | -46.12264 | 2026-09-20 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 026828fa-5ebe-3fc8-8723-b1b20b07936e | -11.85154 | -46.86955 | 2026-09-20 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e738fd21-42e5-3e7a-ab46-72a8c97adde5 | -10.31425 | -50.22025 | 2026-09-20 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| f284fe2a-bdbf-38b9-8d98-6edc145caecd | -12.13271 | -47.0318 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 64a4aade-994e-31b0-bda6-fd9a6827778b | -13.27804 | -46.73108 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaa88cdb-45b4-3741-b964-0dab8a0a5f68 | -6.56461 | -45.58476 | 2026-09-20 03:45:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a59bae68-4879-37eb-b637-b612949e6be9 | -10.60292 | -46.52082 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ab2d81dc-3f07-381b-b619-f46719a09c7e | -7.75874 | -44.88518 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70fdb326-1835-37f1-a33d-1d6937b6cbf0 | -9.22116 | -43.18456 | 2026-09-20 03:45:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 534b1d86-b90e-34ba-9412-4993d586ace0 | -12.12998 | -47.03255 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f6ad5483-71d1-3e2d-83ea-aabb652bad8e | -7.62796 | -46.12165 | 2026-09-20 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b47aa1b2-2f19-358b-b905-323dbdae909f | -9.79371 | -45.05813 | 2026-09-20 03:45:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 674d79f9-aee3-3d26-b904-86bb36b81efb | -11.31781 | -47.29 | 2026-09-20 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 55d055d6-85fc-3eba-98ad-3aae6a43b905 | -9.96419 | -46.54914 | 2026-09-20 03:45:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b165363c-1060-327c-acc3-52dc0fbcbd11 | -7.55418 | -45.4291 | 2026-09-20 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a4b534f8-1f9f-3a0d-a964-bc0acc59c8f8 | -11.23955 | -48.37856 | 2026-09-20 03:45:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7e44fc6e-2fb7-314b-a629-42465ce88069 | -13.01247 | -46.91825 | 2026-09-20 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dbeeee4-6e99-3b4a-b1cb-758429534a94 | -10.49146 | -46.27698 | 2026-09-20 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d426e466-f71d-3d5b-8031-8388cc4577c8 | -6.92745 | -42.90315 | 2026-09-20 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5b596c31-d95f-3d93-b42b-dc14274e939e | -9.25354 | -45.92784 | 2026-09-20 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fa05fe1-114e-3137-8cc8-8129ddf34e1c | -11.10292 | -49.51159 | 2026-09-20 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8e2b9063-2ba0-3b53-a3ae-65d69147df0a | -7.86613 | -44.85874 | 2026-09-20 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b83492c2-cc82-39a6-87ca-c959f69e385e | -10.93268 | -48.31544 | 2026-09-20 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cad92a5c-8687-3bbf-8854-cc0feafcf128 | -11.47654 | -47.78778 | 2026-09-20 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f7d12b4-dfcb-3a5d-9ee7-307a61d19b5a | -10.32333 | -48.00593 | 2026-09-20 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d11e35aa-9b47-34b7-a0cc-d07e12ab6da6 | -12.10884 | -47.02037 | 2026-09-20 03:45:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README19.md)
