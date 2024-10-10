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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d722b52-18e3-3d1f-a6e7-4a3157808b57 | -4.28356 | -45.47588 | 2024-10-10 03:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a42f3efe-6311-3945-ad00-2beb520b511e | -3.908 | -44.86989 | 2024-10-10 03:53:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e8d2ff6-65cf-3585-8ee9-6022617892d5 | -3.81221 | -45.49822 | 2024-10-10 03:53:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fd6d9619-b7a9-3593-a446-0d95babead4d | -3.80737 | -45.49743 | 2024-10-10 03:53:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 2331e56d-3341-3b1f-b0df-0ff027600f97 | -3.75531 | -45.19183 | 2024-10-10 03:53:00 | NOAA-21 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11142eb7-baa2-367b-be4c-7ec5ffcff3be | -3.71892 | -44.96284 | 2024-10-10 03:53:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e00ab67c-f887-30d3-85b6-b6f7ea6a9f88 | -2.18902 | -46.09533 | 2024-10-10 03:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fa68fce-013b-3718-9638-bcc960a0b66f | -2.18436 | -46.09145 | 2024-10-10 03:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36898e68-03cd-39c1-99ed-50a51a23b2e2 | -2.16982 | -45.94032 | 2024-10-10 03:53:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cdd080e9-68f4-3aa6-a764-6923b6a5202e | -2.16934 | -45.94334 | 2024-10-10 03:53:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23b752c2-e458-30c9-a2ce-94c377e09a08 | -2.16469 | -45.93954 | 2024-10-10 03:53:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28dafe0d-405a-379f-b486-da53a64e88c8 | -2.16372 | -45.94558 | 2024-10-10 03:53:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 031a21ed-4178-3768-8424-ec35cb4d2452 | -2.15957 | -45.93872 | 2024-10-10 03:53:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0549e93-64f6-3405-8aab-ba122fa74dc4 | -1.48345 | -46.89791 | 2024-10-10 03:53:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93ded506-cac9-3e52-9250-c378fe29a354 | -1.26382 | -46.35243 | 2024-10-10 03:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6ba533b-a659-38f1-9b87-e242b7a0d94d | -1.2633 | -46.35577 | 2024-10-10 03:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e38350d8-677e-3c18-b21c-e292bcd74225 | -1.26195 | -46.35251 | 2024-10-10 03:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9319b7d-cd98-34cb-ad69-a7f7c47641d4 | -1.26139 | -46.35587 | 2024-10-10 03:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b73daa4-b8f6-3df1-8212-9b1101d53a91 | -3.31157 | -46.98909 | 2024-10-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 370b080d-5c40-3984-a7b1-309a054fbfd6 | -3.31098 | -46.99257 | 2024-10-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f6a6919-8e39-32ac-bacd-3643db0a4179 | -3.30908 | -46.98861 | 2024-10-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 844a1571-865a-35fa-b8c9-7e6db955289a | -3.30851 | -46.9921 | 2024-10-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd9b0515-123e-371c-bd0b-644eefbd2aa6 | -2.84347 | -46.69875 | 2024-10-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a03a250-d68c-306e-9890-d34dc6e6544a | -2.83813 | -46.69791 | 2024-10-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9ef5f5e-0b12-3169-b1c1-59333182925a | -2.64674 | -47.36405 | 2024-10-10 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3704dc19-fcf7-3f51-8ea0-b44fac093eb6 | -2.64611 | -47.36783 | 2024-10-10 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf660a8b-f5e6-3976-abe7-489caee6b273 | -2.36612 | -46.4917 | 2024-10-10 03:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fe73c7d-2bf9-3041-83d6-fadfe9d852de | -2.2925 | -46.97209 | 2024-10-10 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8b86573a-b90d-3035-a940-29cd4e736cd1 | -2.2919 | -46.97572 | 2024-10-10 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e3de65f-e4e1-3657-a23c-430fa37691da | -3.80995 | -47.48971 | 2024-10-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36f35197-cbc0-3188-a629-fab64157c38f | -3.80934 | -47.49331 | 2024-10-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b8012bb-80b4-3a80-ba4a-0daaf4a50a12 | -3.93677 | -46.4501 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38df787c-3e10-3fae-bac9-4740a4181a2b | -3.93251 | -46.45567 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42ec615c-0ec9-31f6-afdb-399fcf86fdfd | -3.93192 | -46.45906 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e393a7dc-0bbf-3b35-9bea-3673cdab6d47 | -3.93162 | -46.44922 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aca89ab-6831-3852-9d11-dc7e025ced71 | -3.93111 | -46.45231 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26a67236-dfdd-3c93-9876-f509d8e2a84a | -3.93059 | -46.45549 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd80061b-df2d-36d5-b2b0-7aefb3b9e5e6 | -3.93004 | -46.45885 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 99fa0724-b3fe-3a3a-af8e-6e9907af1fda | -3.92647 | -46.44837 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b3388aed-0afa-31f9-9d90-ce8012954538 | -3.92596 | -46.45144 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1bcaf081-619f-30e3-b8ad-13e6de2d1bf5 | -3.91667 | -46.44361 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 346cda0e-82e8-3591-988a-7b8fd5e84637 | -3.91462 | -46.45596 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5481b47-1a09-35a3-8f14-883a661f24b9 | -3.91204 | -46.43967 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a12a2fd-2138-3251-80c6-71188978f9de | -3.90945 | -46.4552 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95b1ab5b-6099-3cc6-bb58-8c971a89dcb5 | -3.90894 | -46.45824 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac07cb7d-7133-34f8-8b3b-ae65b040cc24 | -3.90844 | -46.46128 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 537900c2-02ae-3841-91d3-2524cd999c57 | -3.90377 | -46.45749 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 241a0aa2-87f9-362e-883e-ac053e7b241b | -3.90327 | -46.46049 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b14748c3-bd41-3301-9821-9dd29605c41c | -3.90276 | -46.46353 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa86671d-a6c0-31fb-b2d4-efbbade7f545 | -3.89913 | -46.45352 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89982f76-bc98-3089-86e8-ac4722899d94 | -3.89863 | -46.45654 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4754ee35-7e02-334c-90c8-4253cf2a2b42 | -3.89812 | -46.45958 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 621f324d-977d-3802-b1f9-bb61cb72689e | -3.89761 | -46.46265 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d421ec3b-a1ab-304c-9e5a-75fda54f54b3 | -3.89399 | -46.45259 | 2024-10-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bb8e8f7-8804-374f-a33e-08463c7b9842 | -3.69977 | -47.60612 | 2024-10-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a532375-ffc4-357f-b218-08031b8a4f37 | -1.78506 | -47.84496 | 2024-10-10 03:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe1bde58-fb61-30a8-bd59-69ac9a450430 | -1.78485 | -47.84159 | 2024-10-10 03:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f31f6baf-b852-3221-a634-a1c2c77a9626 | -1.78416 | -47.84573 | 2024-10-10 03:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f2d6b6e-6631-3078-b8f7-8f54f87aea49 | -2.94742 | -48.61104 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efbbebb1-821d-37f2-a536-59a994b87507 | -2.45944 | -47.84079 | 2024-10-10 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4deed4a9-1a26-358a-906f-6cff8be3e9aa | -2.45877 | -47.84478 | 2024-10-10 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40722f79-8212-3020-a87d-c81341973228 | -2.42788 | -47.81361 | 2024-10-10 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f12c2666-47cf-3946-a892-179f38e78dd5 | -2.42304 | -47.81003 | 2024-10-10 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58e55a03-3837-3b0b-9f0f-5d0788a0aee8 | -2.42236 | -47.81406 | 2024-10-10 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2a65d85-f8b8-325a-8621-53db95a0a01e | -2.42207 | -47.81284 | 2024-10-10 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5ad15d0-6969-309b-bc5f-3144448b7b37 | -2.23181 | -48.02639 | 2024-10-10 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50a94a9f-432d-35d1-8cac-cdd301354ec8 | -2.22664 | -48.02121 | 2024-10-10 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c41886d-cc64-3c41-9113-3f3b19316670 | -2.22594 | -48.02542 | 2024-10-10 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9410582c-3faa-397f-b436-8c3dd43fa879 | -2.17903 | -48.23449 | 2024-10-10 03:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bfa12eb-cd5b-3c64-8338-cd6b62c8b80b | -2.949 | -48.61212 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 234e42f8-1ad3-3d11-a6f0-937d80fa8eb0 | -2.79133 | -48.56931 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08d9c97c-b139-3293-8323-b8f02f6d2b05 | -2.79058 | -48.57379 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea1cca7a-5f55-33ef-a06f-52de41a45fd5 | -2.78711 | -48.09611 | 2024-10-10 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8130f291-0419-35e5-9440-afd38b9c080b | -2.76021 | -48.64359 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10de197c-8294-3697-8eae-d4eb53892c2b | -2.75775 | -48.6952 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed403209-6584-3039-bf9a-750849e17d08 | -2.75697 | -48.69987 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b754573c-fd57-3409-915e-db1493bf0611 | -2.75167 | -48.69419 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 686bc72d-bff5-3999-881e-2d93f04c2a29 | -2.75088 | -48.69889 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8f91a8d3-0898-3565-8244-a4f8c4a18f11 | -2.74794 | -48.67931 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5a32cb4-792f-3ce4-9329-71b0120d31db | -2.74716 | -48.68392 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb1fb69a-6382-3fc3-b1ac-65d375710bf0 | -2.74265 | -48.6737 | 2024-10-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0551f602-e230-353b-8133-5e9ff1a91698 | -3.72233 | -48.35011 | 2024-10-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1cf68627-883e-3fb5-913e-c4a35ac00391 | -3.72292 | -48.35191 | 2024-10-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dc0b5a68-53a0-3ed8-af54-cb4a688db854 | -3.40704 | -50.33414 | 2024-10-10 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88c49efa-c639-3ad4-8186-3b07d9a5d814 | -3.40312 | -50.33257 | 2024-10-10 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c324f29-53b4-30a0-8f9a-fb9b5881801f | -3.4004 | -50.33298 | 2024-10-10 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41f64ebf-d0c9-3d8d-9960-0356b8586560 | -3.3378 | -50.12765 | 2024-10-10 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8973192e-0943-30a8-8e6b-e7b65f29f52f | -2.99204 | -49.53178 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b9be65d-7775-3108-b807-aef767241a77 | -2.98565 | -49.53079 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3bc9b19a-43f2-38f3-a11e-bdf1666d3eb5 | -2.98326 | -49.53371 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c3b5ff1-0da8-3011-b0eb-9297288673f8 | -2.95164 | -49.19669 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b729e0d-5618-3ac5-8128-8eec824686ca | -2.95081 | -49.20166 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be58d340-f0da-3d81-a483-8c6f4ceaf79a | -2.94759 | -49.2081 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 041e801e-ef82-3631-99a8-ded20884d3c7 | -2.94673 | -49.21307 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 464181a1-8f11-3e1b-8f42-b89581f27da1 | -2.89682 | -50.39621 | 2024-10-10 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3dde660f-f4fd-34d9-98e1-27577547b0ea | -2.47508 | -50.24594 | 2024-10-10 03:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 19b227ff-7021-3eb0-8a28-6e2d0cb5282a | -2.46835 | -50.24491 | 2024-10-10 03:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 86c4d30e-2ad4-3585-a1b3-73ffdd80349b | -2.99053 | -49.52943 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 16a44738-5982-388b-8d22-76321775bee6 | -2.98414 | -49.52844 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f803aa8-f97d-3bd5-b252-4fd1ad1a4d70 | -2.96523 | -49.29331 | 2024-10-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README41.md)
