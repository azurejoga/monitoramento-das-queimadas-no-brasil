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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8674e0ad-4e62-3a19-8577-0a0846e9673f | -9.96055 | -67.21803 | 2026-09-10 05:50:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37099cc1-bca3-3701-8288-448fc7fed0e8 | -13.30818 | -61.66199 | 2026-09-10 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| beb8bc14-0624-397b-8d24-43a5749549e4 | -13.28662 | -61.62644 | 2026-09-10 05:50:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfd39c5f-3481-3932-806f-ef34d340dc86 | -10.85864 | -60.83359 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ff7d5dd-ef62-3996-bd3d-f6e82fb2202e | -10.85486 | -60.83303 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3e3a54e-e6a9-3122-9894-6c4913476e42 | -10.85419 | -60.83762 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6615debd-f704-33f4-a3aa-e69b9b292468 | -10.57759 | -68.77155 | 2026-09-10 05:50:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8a02a7b-ae8c-3af2-bd8f-4ef4996b904b | -9.48614 | -68.8709 | 2026-09-10 05:50:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc5dbcd1-f19d-3873-9877-54c537d9e9c3 | -12.4668 | -62.57106 | 2026-09-10 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 894439ce-c3e7-3a9d-97c2-9bb05c92d6a3 | -8.88257 | -70.83953 | 2026-09-10 05:50:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bdd182f8-b792-3992-9641-210804be7562 | -9.96396 | -64.76134 | 2026-09-10 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c07b688-9681-3388-a39f-753b5d06f6e0 | -10.85108 | -60.83244 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91078e31-60fb-3122-8d12-555a49494db0 | -11.40559 | -62.11529 | 2026-09-10 05:50:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9c10d6e-96c7-3a0a-b87d-350ff5ad2855 | -12.1586 | -64.13416 | 2026-09-10 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6c672e7-0b53-3bdf-bc45-2876b609376d | -13.29123 | -61.80562 | 2026-09-10 05:50:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d9a0197-c7f5-3e28-82d9-6ad89957349a | -9.37755 | -68.82466 | 2026-09-10 05:50:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 505f8b64-2c08-3c5e-b2f4-614e796af93f | -9.32222 | -68.19231 | 2026-09-10 05:50:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaf11afa-134a-336b-8011-23b5a198d84f | -10.19038 | -68.76815 | 2026-09-10 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec43069e-bb43-37ae-bdd7-c42032fca9ff | -9.30536 | -67.69674 | 2026-09-10 05:50:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0548d261-2903-3699-a647-f4f361ce9df9 | -13.32262 | -61.64109 | 2026-09-10 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24bdbd02-4a7d-3a60-a4de-8de4b2fea297 | -10.6534 | -58.76795 | 2026-09-10 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 152de528-6b8c-3335-bace-9721235562c2 | -13.28753 | -61.80507 | 2026-09-10 05:50:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb5b6bf3-5feb-344b-8901-b0a58af1ad24 | -11.41809 | -62.10478 | 2026-09-10 05:50:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43bbd201-ffd6-3099-bfe2-e4623f626fb5 | -13.29492 | -61.80618 | 2026-09-10 05:50:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5653cfe3-28ce-3046-9146-1d88dc3ac6e2 | -12.46732 | -62.57179 | 2026-09-10 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8e6c21b-46fa-38fe-8fd2-a3e561d580b5 | -13.32328 | -61.63656 | 2026-09-10 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63506055-164d-30bd-aeb7-00056016047c | -11.40498 | -62.11936 | 2026-09-10 05:50:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb1c5a12-2d19-3719-80b4-dc4d9e53368e | -11.42532 | -62.08078 | 2026-09-10 05:50:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40a26cb6-2d4d-3f30-ade5-0a3c0f0537be | -10.9883 | -60.65897 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83a9c18a-af59-393a-b487-5676f41c7043 | -10.19418 | -68.76884 | 2026-09-10 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd011077-6e2e-314d-9e27-cdc6da9d1c7a | -10.61917 | -67.92565 | 2026-09-10 05:50:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73ed7e52-6470-3127-9cbc-2f3d6857a457 | -10.6 | -60.78553 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e9e6dde-9781-33e1-9c09-4a880dba5e5b | -11.42166 | -62.10532 | 2026-09-10 05:50:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 125a89b1-a4bd-3120-b3f2-0167f8c1d256 | -10.49513 | -59.6041 | 2026-09-10 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2660d1af-7e21-3e70-a133-97a016707b2f | -10.11758 | -68.60901 | 2026-09-10 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2df147de-a7ab-3c8c-a6d5-aab75051f0f6 | -10.85796 | -60.8382 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d4321d1-0f61-38e6-b023-d3da3dc42db8 | -9.16867 | -68.20654 | 2026-09-10 05:50:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26e262c6-3907-316f-8c7c-fad8532906ae | -9.43459 | -67.57429 | 2026-09-10 05:50:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ee4022c-8f6f-3f84-a8e4-531ef4677a80 | -10.62279 | -67.9263 | 2026-09-10 05:50:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f54c8dc-9d98-390b-bfe2-292bfd6f14cd | -9.91786 | -67.8753 | 2026-09-10 05:50:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d57e7a34-766c-3704-bdee-b6c5b21ad94e | -13.20331 | -61.82624 | 2026-09-10 05:50:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53d1b617-88b0-3379-8b51-4fed74c2e038 | -10.99213 | -60.65952 | 2026-09-10 05:50:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 042f8684-89a4-386a-baee-fed532866b9b | -11.40794 | -62.12396 | 2026-09-10 05:50:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4970fea3-6396-3098-be5c-41476b3d8d2f | -12.15805 | -64.13776 | 2026-09-10 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9b0f79e-3db7-3303-904d-9b736902c33e | -13.32701 | -61.63712 | 2026-09-10 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78d169bc-aeb5-3ddb-acee-c6e3f8d67f5a | -10.85932 | -60.82898 | 2026-09-10 05:50:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0f29a84-af72-3212-8f5f-e1d60f9242e5 | -9.84748 | -66.46085 | 2026-09-10 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b35b34e-4185-324c-a774-2912e027fd66 | -9.1498 | -68.25012 | 2026-09-10 05:50:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b29ffc7e-75a8-3534-bcda-b5919da4bfe9 | -12.86 | -44.36 | 2026-09-10 06:00:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a79cc64c-4602-3d2f-a8fe-ae9efb05369c | -12.83 | -44.35 | 2026-09-10 06:00:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff2adabf-765c-3301-ba50-7afb5e4bccf1 | -2.72413 | -57.62181 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45fab4c6-83d5-3f03-b5dd-f84706a06eaf | -2.72491 | -57.61666 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e9cba88-81c5-33e5-bcf1-9b1d769995a6 | -2.72694 | -57.61979 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd3c770d-65e5-31a4-88c1-b253b4f142ce | -2.7333 | -57.62075 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e02ebae9-b7aa-39d0-85b8-05ff6606b1be | -2.73528 | -57.63391 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c471f47e-8159-3e2d-8c08-5c2013f19840 | -3.59368 | -59.07976 | 2026-09-10 06:05:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6978c148-966a-3083-bb1e-adb2bd3f4b45 | -2.72619 | -57.62493 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 815b9ae3-5b67-3ffc-b23a-20ecfc4c55b8 | -2.72892 | -57.63298 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7b711910-424a-3aaa-9ed9-c3ec71501e6b | -3.3688 | -59.43393 | 2026-09-10 06:05:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4be56757-ce94-31c8-be01-dd69e6e392b4 | -2.73606 | -57.6288 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68e58928-7b27-372e-b498-d58842410420 | -3.36939 | -59.43 | 2026-09-10 06:05:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7cd9ccc-513d-3e6f-b347-0884b5a02e41 | -3.41638 | -59.23244 | 2026-09-10 06:05:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 639b96b2-9c73-37a4-bdef-da258126bc2e | -2.7297 | -57.62786 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36a47de4-20c6-38d5-b226-b3e128e1f1d9 | -3.59274 | -59.07896 | 2026-09-10 06:05:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 701d9753-ffcb-3410-b795-f9fd43efa806 | -3.41059 | -59.23158 | 2026-09-10 06:05:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cf1db96b-73bb-36b4-b531-754a447d46fb | -3.43652 | -59.25612 | 2026-09-10 06:05:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8faacba6-35cd-37b8-b656-b1cb09ac2373 | -2.73255 | -57.62589 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7e15aa3-60ea-3e93-8ce1-66fd8771db97 | -3.5878 | -59.07897 | 2026-09-10 06:05:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61402975-8f72-3802-96f6-44bdf68fea14 | -2.73816 | -57.63197 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6b219083-1868-30fb-be41-0afe23e098bf | -2.73049 | -57.62275 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 711eb6fa-41b6-39c9-9454-8d40be1ecf68 | -2.7318 | -57.63101 | 2026-09-10 06:05:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d36f249c-a182-3985-91d5-f3e129e5f153 | -3.53412 | -58.9542 | 2026-09-10 06:05:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f304b6d8-b520-3938-a197-1d27b8d10f4d | -3.54004 | -58.95502 | 2026-09-10 06:05:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51cf9f70-f520-3c77-99b2-1491b656b51a | -8.6821 | -62.46041 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73594ebe-9785-3d6d-8ca0-e3f863acc710 | -9.14859 | -68.25188 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a55bc788-708a-3234-a39b-b4d609f4cddb | -9.19144 | -71.80373 | 2026-09-10 06:08:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5aa25924-dd48-3ed5-9e97-10d420977262 | -8.89969 | -61.43723 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 278d0ca5-e0f6-3c7f-814c-241c9e7dc976 | -8.90512 | -61.43789 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abc7916c-9a83-3c04-8de7-597e8279c061 | -8.87934 | -70.84219 | 2026-09-10 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0afe04bd-ff0a-345d-b784-cc193b2790af | -8.68715 | -62.4611 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39446654-ac30-343d-b3c2-a4d9c3d61a13 | -6.81427 | -60.13522 | 2026-09-10 06:08:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c24d3e18-829f-3729-a7a0-dd0a79a832fa | -8.99946 | -65.40611 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 48bbd112-dca4-3cce-a5b0-2fc30718890b | -9.13877 | -64.41194 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9d569a1-2db6-314e-bf2a-960627c86382 | -9.19905 | -65.77453 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58a730a2-d305-3def-94e3-d9aaa2e68f31 | -6.7791 | -58.89199 | 2026-09-10 06:08:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c79f4951-bd16-3ecc-a88d-aaf449886cd6 | -9.5784 | -67.81659 | 2026-09-10 06:08:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7759674b-0258-3a5b-aec9-066edb23273c | -8.99368 | -65.41678 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a0f052c-bf9b-3832-bb98-606dad05d8d9 | -8.68249 | -62.45746 | 2026-09-10 06:08:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20c9f190-7b7e-37ef-a716-3b0da4f461a0 | -6.55112 | -62.88751 | 2026-09-10 06:08:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f8ca916-237c-323a-95ec-e6ef391e3ade | -8.89026 | -61.42534 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db7f95ef-953d-3d71-b220-92bfb551fcdd | -8.54289 | -70.4777 | 2026-09-10 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3bad0cc-2f47-3442-9a19-5440f413fcd6 | -8.98591 | -60.58003 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc8c13a1-d641-3b3c-9edd-6ab04738d392 | -8.8265 | -62.48759 | 2026-09-10 06:08:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29b79422-8b11-3889-b74c-b6f89017a110 | -9.37737 | -68.82436 | 2026-09-10 06:08:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00bd5de9-b4b3-311d-8cd0-cbc6f35bebc9 | -9.1527 | -68.24845 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 911d080c-adb4-3a97-aeb8-c29924bff05f | -8.88265 | -70.84271 | 2026-09-10 06:08:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cab5f0ba-3b67-3b84-80b1-617b6fbb0f59 | -8.89238 | -61.45047 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8bfd861-42f8-34e7-a812-99fd434412a5 | -9.08413 | -67.86777 | 2026-09-10 06:08:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a1b8cb3-0871-32f6-a05f-469c6b7bf630 | -8.98643 | -60.57607 | 2026-09-10 06:08:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f982c91e-8047-3f6d-a01c-d254d4682324 | -8.62812 | -66.50988 | 2026-09-10 06:08:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README43.md)
