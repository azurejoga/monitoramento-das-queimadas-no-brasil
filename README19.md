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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24dbfceb-6247-3d41-8191-d056a0dcd30a | -12.59878 | -48.22327 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b3260a5a-1144-3d52-927b-5f82a96c5904 | -12.84517 | -48.07684 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17e8e408-42b2-35e8-b957-d2072612779a | -11.01454 | -46.85236 | 2025-09-01 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 753aa968-ad9b-33c2-a47e-60eff188c010 | -7.95398 | -46.44995 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 951d2bb3-8eb0-3212-8da2-e3ec706fcc58 | -11.3737 | -43.61043 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0055604f-9597-3c44-9a42-161814972240 | -13.49016 | -46.97631 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83a25156-a407-3d98-9671-de52d96e85a0 | -7.95312 | -46.45451 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6797a0f3-ef0d-3524-8fd0-f60b53d30433 | -13.37148 | -46.94295 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c6500eb5-29da-371c-8c5f-d55b07ed191f | -11.89648 | -46.69306 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 47222f1d-23af-3fca-b317-b1ea15e0668d | -13.47686 | -46.98823 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d541b962-259f-3ddb-96ee-e747661973d7 | -11.95635 | -45.84241 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 100ab265-2dde-3a4b-b6ed-39213b6f39e8 | -13.47804 | -46.97951 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a237e8e-d016-3a69-917a-12a9569a735c | -14.047 | -44.58064 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 644a93c7-e0e3-3773-976b-bac4f19bb4f3 | -11.37593 | -43.57162 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ba5216e4-3c41-3057-a6a6-7fa87d1fe796 | -14.04681 | -44.59456 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e292c936-9c0d-3eef-b107-fe13979fb9bb | -8.89368 | -45.09962 | 2025-09-01 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db244983-2825-3e63-a83c-ef63b3538861 | -14.0442 | -44.59585 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 653499bf-5a62-3bcd-9c18-649eb0d9958c | -7.40093 | -47.44215 | 2025-09-01 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fe625e21-dfde-3407-ac0b-9b06d6400732 | -7.62419 | -42.65446 | 2025-09-01 03:45:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 051c53fc-021a-3813-9722-49a6214ad963 | -11.90634 | -46.67932 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f75c45b6-7aef-3f64-9e6d-ed1cc8bccd1a | -14.02257 | -44.60802 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f436c5f-739b-37af-9d82-5788bb9216f4 | -13.36588 | -46.94228 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9a7f17bd-0c12-3bde-bde5-139beea9246f | -11.89515 | -46.73797 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d2364508-93c2-3f22-a37b-370313f19f88 | -12.56242 | -48.21638 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| efafeaf2-f85d-3ef7-839d-330e24c3c4a4 | -11.02908 | -47.06142 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6cb9898-95c6-3388-8387-338e19189526 | -11.37284 | -43.6152 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 171dd470-75a2-3ed3-bda2-c874179ec4d0 | -8.01501 | -44.05658 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f872d87-c3dd-3307-ae6f-c5ffc49190a2 | -12.5779 | -44.80635 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52de31c2-a270-39d3-b57d-85c2d66a65b7 | -9.66992 | -47.03984 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 222a0228-1d11-36e8-9e8b-735bc041c41b | -11.95917 | -45.79835 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad7164c9-3e4e-3788-9924-0c4cea5e0a4b | -13.37614 | -46.94698 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce74d9fe-6729-3ddc-b85e-b949048e1616 | -11.04589 | -45.15073 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 864bc5f2-3980-3f8d-bece-68ebd24245d4 | -11.3674 | -43.61908 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89335431-48de-3822-bd72-690abf883785 | -12.79713 | -48.08687 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e52e18e7-423d-3350-9f22-1879d2b7b480 | -11.85126 | -46.78511 | 2025-09-01 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6160c50-1d2f-31ab-8541-a03e88b001a7 | -11.0856 | -44.6312 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 82cf8b64-0168-3a17-a17c-ef8d99d0a757 | -9.26782 | -47.1107 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cecc044-07c8-3a10-8743-02ea795640cb | -11.04647 | -45.14763 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 557.8 |
| 6a910478-f9d7-3bd4-baa2-88c87d7d2004 | -11.78848 | -46.46069 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e96b5714-818f-3b19-847b-e8273d42f565 | -13.33714 | -46.97199 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83f2e332-c8a4-398f-af71-06d07be6c8f7 | -11.89195 | -46.74504 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a01ee0d5-cd3e-3f59-a307-c0dcdc5f225a | -10.60497 | -44.33284 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a318e943-7c01-3ec7-b0b5-342fec49a065 | -11.80338 | -44.94191 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9285e4f-2fb1-302e-956b-a0aab4627788 | -11.48733 | -46.8075 | 2025-09-01 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61a8d7d0-4135-3854-926f-f6adf40faf55 | -11.04314 | -46.8965 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8ca3f18-6fdb-3d1b-ab30-5fcb7ced27e4 | -11.37423 | -43.58104 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 46756c6c-9832-3db0-8441-bd72c51a622b | -8.19954 | -46.78256 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| cc5865fe-26fe-35a5-b241-1ef4c8201f9b | -14.04408 | -44.58358 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d725a6c-ac98-34de-a847-f20f29ba88b5 | -8.06091 | -48.42622 | 2025-09-01 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a4366d62-d416-3a14-98bb-8acbca38aa95 | -12.09821 | -44.72363 | 2025-09-01 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da430601-59fe-3fae-9496-93583a235fad | -8.06206 | -48.4202 | 2025-09-01 03:45:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c753270c-8ac7-3f2a-aa40-1e1ade99b311 | -14.04506 | -44.5785 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e9c38107-1799-3409-8289-748d8cc4e83c | -13.49205 | -46.99538 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e5c7cf8e-75d3-386d-aa41-6bd1f528bb94 | -11.37199 | -43.61996 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d285272f-facf-3cff-b2a8-e8af3379c265 | -7.45402 | -44.80904 | 2025-09-01 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d512dae9-b9d7-34bd-b3bd-3b000aa4ed9d | -11.05214 | -45.14562 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34f90e4c-53ba-32cc-bb1d-2cad85375dbb | -13.6984 | -46.90788 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f12431a7-1568-30e8-be90-812621ef3cf1 | -11.03725 | -47.05021 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f4e70e6e-c4a5-3049-b26c-39b8c7ca5386 | -7.69961 | -45.00154 | 2025-09-01 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cea2ec78-06ff-35f5-b026-61279a8f43cb | -14.04422 | -44.56955 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3790e2f8-3b92-311a-bdb7-0af70d90cdc0 | -7.93758 | -46.44837 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6aef33aa-05b2-3581-b645-fad015b9b883 | -10.05262 | -48.09821 | 2025-09-01 03:45:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6cdc5887-5f31-33ad-94e3-e027d33dea6f | -12.02271 | -49.70967 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bbaa4bc-eacb-3750-9eca-179ffe83e343 | -13.16578 | -45.28889 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 39bc249b-fe2a-3343-a1fb-c3f8bfde3b57 | -14.02536 | -43.90366 | 2025-09-01 03:45:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6b414e4-0bba-3e48-a1f2-ae7e659e8baa | -11.03805 | -47.04607 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f826c2f4-1ce9-3175-9e91-73618e8afdd4 | -13.9966 | -46.31961 | 2025-09-01 03:45:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43f3d51d-3a70-3af9-8abc-c32751f612b5 | -11.8986 | -46.68964 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1c94b31-ee0b-3cea-b293-7d2d8d24e7ab | -12.56903 | -48.20984 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cbf49a3c-12bc-3e51-aa35-c78c50a18905 | -8.19768 | -46.77529 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| faa5c645-87c5-3801-aa10-66476317884d | -10.04422 | -48.10785 | 2025-09-01 03:45:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c2ce4327-2eff-3260-945c-faaac3d6f9f5 | -10.12124 | -45.76502 | 2025-09-01 03:45:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7e4373a-b74b-3ee7-976f-dc41b43bf094 | -11.04766 | -46.96535 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85552f82-2315-34df-b54d-788d82738245 | -11.80114 | -46.42463 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 45cf93c4-676b-3648-85b6-e35ca7ba00fd | -14.00177 | -46.32101 | 2025-09-01 03:45:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 19d9120e-0abb-301a-b8f5-75e550082e1e | -8.47436 | -45.17737 | 2025-09-01 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6a950044-6838-36e4-9cad-2a1ea752212e | -13.37133 | -46.94246 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1da9459a-c70d-34e3-a19e-632559e4f864 | -14.04513 | -44.59077 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d1f74787-28cd-33cc-b462-e92ec6ef6097 | -12.81149 | -48.07716 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ade726af-3c8a-3837-9c4a-c5570a4213cb | -13.5219 | -46.98948 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24f4f8f5-646a-37e4-92a7-615ef69cea26 | -10.60113 | -44.32639 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| b38c37c7-1ac4-3185-90be-2dc7f602a75d | -8.33703 | -47.43838 | 2025-09-01 03:45:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 217e9cb8-d153-35ed-96ce-5a348e661a41 | -13.69323 | -46.8734 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 484946de-738d-35c4-94aa-522cf64d6ffe | -11.9009 | -46.67757 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ab5d239-9973-3d17-ba56-004eb9ddae6d | -13.48918 | -46.98117 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0b751d7-4c9d-38bf-9e33-95ea087a391d | -9.63412 | -46.6059 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 716ae79c-ed8a-38fd-8f4b-8462a76aee82 | -12.31244 | -45.68382 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 667488e1-e17e-3cba-b17a-2cbd697b59f4 | -9.30843 | -41.13674 | 2025-09-01 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5116d125-0972-3455-be8f-8c9d1b8c53b6 | -11.80852 | -44.94436 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e3bd870-e67c-3e33-99dc-5f9ff9e13d96 | -12.57538 | -44.80791 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73edced4-cb55-3d10-b3f0-2f80e198efff | -7.8882 | -46.99773 | 2025-09-01 03:45:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e756509d-77cb-3064-9311-eb82debf234e | -7.6309 | -46.54659 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63924e9e-0a7c-3b21-a39a-c7326f163243 | -10.60761 | -44.33147 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| ce85ba08-bba6-3480-829e-9fde26be45f2 | -11.33845 | -43.67414 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64cc265a-55f1-341e-a76f-8a6667f8c0a7 | -8.88109 | -47.21152 | 2025-09-01 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7230fe91-757c-356a-8d58-1c09007747e6 | -9.1537 | -45.22084 | 2025-09-01 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9775e497-ae5e-3d7d-a74b-985543742a92 | -13.16193 | -45.28213 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d4dbf24-1ace-316d-b64f-b70eeed6ac08 | -13.49286 | -46.99137 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b0768cbf-2b70-373d-adf5-573401a52d0c | -13.69225 | -46.8784 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c809a5e2-056d-3736-9ebf-c0b35ffe73de | -9.66827 | -47.04833 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README20.md)
