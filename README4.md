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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36b210ef-801f-3c5d-924e-42ba2c153fbe | -8.10968 | -47.09636 | 2026-07-11 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3caf048b-f297-3a14-aa1c-ab772046774c | -7.0137 | -45.41485 | 2026-07-11 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8da81020-128e-3b75-b5ea-226d2d139096 | -5.11445 | -43.74824 | 2026-07-11 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f164d0de-cc51-3ce9-a8c6-4d9fee90e179 | -8.50563 | -48.06816 | 2026-07-11 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9def0ee7-f57e-3c24-8b81-28c7b9d63966 | -4.82069 | -42.97339 | 2026-07-11 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0aaf044f-52ea-384e-aab6-47c6af020120 | -6.50033 | -42.21461 | 2026-07-11 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 229d23c8-5fbf-3d30-8856-5966d5fe572e | -4.82346 | -42.97734 | 2026-07-11 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c486e051-f11d-3cb1-9d59-a4de27fb61a6 | -7.00891 | -42.7745 | 2026-07-11 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bbe06917-6335-3888-8ba4-85dde5e4018d | -8.35471 | -45.3993 | 2026-07-11 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b134610e-ab8b-3b78-8884-1d90268c228b | -5.93857 | -46.35282 | 2026-07-11 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44b34a37-9806-38bc-b335-7918c12e9791 | -5.34465 | -42.69298 | 2026-07-11 04:14:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a845d683-fd2c-3e8e-af3c-4911a0863bd2 | -7.01551 | -42.77553 | 2026-07-11 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1ee18e85-a1d4-362e-92c2-9310e15caf58 | -5.43812 | -44.67738 | 2026-07-11 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3050ea93-a7e2-3a40-bc9d-a367b671337e | -7.8973 | -48.26061 | 2026-07-11 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 869c2e24-2d56-3ba9-a1bd-05485a4482e8 | -4.28445 | -48.3599 | 2026-07-11 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72a393c7-3d80-3069-a382-0ff40f8ddf81 | -9.40525 | -37.81652 | 2026-07-11 04:14:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b7bfda2a-fa99-3d25-8fdf-f29ed4f94280 | -4.61534 | -49.05025 | 2026-07-11 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65938875-9ca0-31e6-bb8e-ddf4b05d296f | -5.13176 | -42.87817 | 2026-07-11 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82d1cc29-e7fd-36fd-89d2-9ffe4af3fe4c | -6.67243 | -38.8482 | 2026-07-11 04:14:00 | NOAA-21 | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f9756866-36ce-3fdf-90a4-fe645c4e1fee | -9.40443 | -37.81855 | 2026-07-11 04:14:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6e60d1da-fb0e-342a-a3df-876ee718e67c | -6.07298 | -46.99453 | 2026-07-11 04:14:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea89b0bb-72b9-397d-b825-aaedd92ee516 | -2.76856 | -48.57417 | 2026-07-11 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3628a3da-6e8c-3e9b-9309-b3d937dba0f4 | -5.13576 | -37.56749 | 2026-07-11 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0559a25a-a0b7-3a5c-bb65-424b4018cad9 | -14.50988 | -46.53917 | 2026-07-11 04:17:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11e38490-3dfb-3eb9-a537-55286267a0b0 | -13.38535 | -54.34202 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60abee24-4739-3fbb-be81-f66ae98328d9 | -13.39073 | -54.34319 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12fe9663-c837-3456-9f32-f26dc0addc8c | -13.89751 | -43.7883 | 2026-07-11 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0602c2f-255a-3da3-926d-a83eaa7e3d5f | -13.25661 | -45.11527 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dd4641f-2fbd-3dcd-aad8-6de921be4a02 | -12.45272 | -49.58168 | 2026-07-11 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df5d03b3-67e5-39fd-a236-86b0377bf60c | -13.37101 | -54.35783 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7efcc362-b052-3e73-80c3-b87e73bdc3ea | -13.2583 | -45.10466 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e1411c5-6c06-3e01-a450-bbc7de2de421 | -11.83761 | -48.23884 | 2026-07-11 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4a72925-d9bb-3156-afe7-76c8d5d8dbde | -10.0964 | -47.97918 | 2026-07-11 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 46e51444-2e19-3be5-a27f-e4b528c0888e | -13.25555 | -45.10058 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d7a7ba0-2d4c-3845-bf10-5bd5d3d4acb6 | -11.43057 | -47.59302 | 2026-07-11 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 002e00fe-f924-3ab5-b653-90731d3fc576 | -14.74113 | -48.1974 | 2026-07-11 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5a6e51a-b49e-3702-ae8e-afd715b2f148 | -17.93856 | -42.79705 | 2026-07-11 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df4dd028-2116-3581-8c99-5a3b1971762a | -10.84858 | -45.04009 | 2026-07-11 04:17:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 298f397f-4a29-37f7-a2d9-30acb30f3a13 | -10.74123 | -47.26562 | 2026-07-11 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5367b16-1ca8-37b1-b80a-7e552f93c186 | -11.87828 | -47.65619 | 2026-07-11 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 85347509-0434-305b-a4e0-b58199c5df8c | -13.21677 | -54.30507 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70dd0542-a442-3daf-8843-0f6785b2c562 | -13.38464 | -54.34566 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 560cfa71-f1d2-3638-bccb-a65cc6f4baee | -21.10242 | -57.46607 | 2026-07-11 04:17:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd06b1c5-08dd-37ab-b3c6-9eaf5559a2c3 | -16.3301 | -48.06738 | 2026-07-11 04:17:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f88c49b4-08cd-3cb6-bb51-e81838a6a3fc | -13.39002 | -54.34684 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e5c2a89-d7a2-34e0-b06c-ac0913492154 | -11.71061 | -47.80311 | 2026-07-11 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1919c17e-0549-3cf2-a892-465b440471c4 | -22.9171 | -49.20235 | 2026-07-11 04:17:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b06c84ba-692c-394d-ae2a-7c7f1d9cd47b | -13.25774 | -45.1082 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9facf39a-510f-3a85-87dd-7244f611218c | -13.38108 | -54.3638 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 363d67a4-084e-395c-b013-008ec6caf7f4 | -15.68592 | -47.51149 | 2026-07-11 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b31cf3ec-2ade-378e-b6b0-509e2f643c65 | -20.04548 | -47.79813 | 2026-07-11 04:17:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6fec640-27fd-32c2-8105-0a00473aade9 | -13.25443 | -45.10765 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78771df3-6fc0-3cbe-9c45-38f4e51804a6 | -20.84953 | -50.24701 | 2026-07-11 04:17:00 | NOAA-21 | NOVA LUZITÂNIA | SÃO PAULO | Brasil | 3533304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d966a2aa-f2c4-3577-9a7f-891697e58ed9 | -13.32155 | -54.34353 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 783a9ab2-4f9e-31fc-9927-45b599db6b0a | -21.85332 | -41.39994 | 2026-07-11 04:17:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 320703e8-0260-3976-b178-c1c52beef9db | -12.6868 | -46.51226 | 2026-07-11 04:17:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 070a8605-5ff1-3525-877e-2ceb420fc389 | -13.36741 | -54.37609 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0121177c-490d-353a-84f5-1e165b131960 | -15.58785 | -46.81049 | 2026-07-11 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ed13702-c3a5-3bf3-90a3-e10e1dd16d7d | -13.85046 | -44.9741 | 2026-07-11 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e43ac6f6-d2cc-3306-9af2-f879b1b2fa4a | -12.46013 | -49.5868 | 2026-07-11 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 558efa23-fb8b-3697-8753-76fa455c763e | -12.45674 | -49.58244 | 2026-07-11 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a56c7665-1ab1-35e8-9f84-bcc871c29d5e | -13.37457 | -54.33976 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7ff32b4-fdf9-393b-b063-884f06e5c185 | -13.9774 | -53.92573 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2453a40d-e10d-3416-abfd-ef866ddba0d2 | -15.52815 | -45.91922 | 2026-07-11 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e6bca82a-09c1-3076-8b70-e64af07dab8e | -22.67649 | -43.47969 | 2026-07-11 04:17:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 942431e0-f979-338c-9831-d34eb64d1d4c | -21.42714 | -47.06673 | 2026-07-11 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bdffaa4-6ed3-372d-b130-650bf98a9170 | -13.21606 | -54.30861 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d09875e-989f-36f4-9315-ff99587c3232 | -10.74554 | -47.26197 | 2026-07-11 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38625ada-efc5-33b8-90b8-4ee410ac79cd | -10.12073 | -50.17414 | 2026-07-11 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b13fb360-4808-3488-877a-dc19c0afbd1b | -13.97222 | -53.92459 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 825982bc-e53c-3593-8363-036b56cb6ecf | -10.33907 | -44.3039 | 2026-07-11 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 838532e1-15fd-3459-ab6c-8562a5eb4e4b | -12.68276 | -46.51547 | 2026-07-11 04:17:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a20d29d9-99bb-326e-92f4-00ba8c8f7fe4 | -22.3771 | -49.7931 | 2026-07-11 04:17:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cf5a11c0-67c3-32ba-aa15-4c49b19380aa | -10.38522 | -49.58096 | 2026-07-11 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dc698ee6-794e-3417-9591-50b6ab4603cf | -11.88191 | -47.65679 | 2026-07-11 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 26b68548-581d-3615-8a88-928aded3444b | -12.82646 | -44.34399 | 2026-07-11 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37a486ca-21ae-3baf-8f70-16c6574b0475 | -10.09563 | -47.98374 | 2026-07-11 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1844d4e-95c9-3e7f-8656-3ffe884581e8 | -12.82425 | -44.33644 | 2026-07-11 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94b6b051-458b-3ebe-a64b-aad7df342ef0 | -18.02682 | -41.83095 | 2026-07-11 04:17:00 | NOAA-21 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a5bd2962-0094-3b06-a058-1973ff3f0636 | -13.25168 | -45.10358 | 2026-07-11 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0581a76d-1d9a-385e-ab68-e73a8a5ab248 | -23.36459 | -46.16983 | 2026-07-11 04:17:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| eb57e1c6-174e-327b-ad39-51c9199c7af3 | -13.38859 | -54.35413 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41f0ea58-2596-31dd-bb9d-f40c3f2473f2 | -22.92054 | -49.20301 | 2026-07-11 04:17:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5d5f805-ef1a-34b1-a941-8d124d6b7001 | -13.37853 | -54.34815 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c69a205a-43f1-30a0-8b2c-78a227cb45a3 | -16.33276 | -48.06901 | 2026-07-11 04:17:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36c7c8be-526c-38b1-b5c2-4c7192ebd53d | -10.40392 | -49.44691 | 2026-07-11 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36eeaba4-407d-37c7-907a-dbd0b9f574fe | -13.37386 | -54.34335 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 181506d7-663e-37de-80a3-d982c29cffda | -16.87208 | -47.57134 | 2026-07-11 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07d3cf52-f6a2-3c1e-9834-99c8f5adc4d6 | -13.37782 | -54.35177 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 492104c9-cefc-31a2-bf1c-464c8f05cd0e | -14.72958 | -48.19999 | 2026-07-11 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bdc629a-e543-3b04-bb25-2cb805b6e1e1 | -12.82701 | -44.34048 | 2026-07-11 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b4e1162-947e-3046-822b-03f2a358c09c | -13.37711 | -54.35539 | 2026-07-11 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29a288ef-1620-33e4-ad39-37e817fcb781 | -23.23575 | -46.59228 | 2026-07-11 04:17:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5990cf53-3f51-394b-b204-a1a49d6cf22d | -13.31691 | -40.46488 | 2026-07-11 04:17:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 57b32ca4-9ba0-386b-b88b-6f6620692f42 | -22.38063 | -49.79382 | 2026-07-11 04:17:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6178c465-d89b-3317-a1a7-95214ce676d0 | -10.40804 | -49.44769 | 2026-07-11 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8e1f28d-e4f2-3c80-bdce-6828c7af7700 | -14.98733 | -45.4243 | 2026-07-11 04:17:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 458114d0-48ac-3332-9157-66995b4114bb | -21.28175 | -41.8132 | 2026-07-11 04:17:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0ac066cf-1a74-3148-b212-5f78cb72a64f | -12.68618 | -46.51606 | 2026-07-11 04:17:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf7e7e29-1e4a-3b42-997b-e5cfa4491916 | -13.76054 | -46.26385 | 2026-07-11 04:17:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README5.md)
