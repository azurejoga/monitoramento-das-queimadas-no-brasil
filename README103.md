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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7846ecae-b74b-3e51-841b-a2a897972d1e | -2.75588 | -54.09013 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74a5feb2-cd66-3f66-ac80-29a34fba14d9 | -3.85056 | -51.34157 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0dfe29a-4a3c-3c94-8929-c49bb28233cb | -3.79787 | -50.611 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6224433d-dc46-3e6d-af16-8980f30dcbed | -3.31363 | -53.8663 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f17ce80b-0e45-314a-bc4f-c47b2a1a97db | -4.8825 | -49.27995 | 2026-10-08 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9587b46c-aae0-3509-a243-51bad56a539b | -8.08504 | -55.29525 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afabd2f3-684e-3016-b1e2-28335b8ac6ec | -4.05777 | -55.32438 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 886cfcbb-46bd-32c0-a7ad-d88118f52e64 | -3.01966 | -54.06134 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 788b30c2-6eee-34f5-8469-2c4797e249cb | -4.40334 | -49.95699 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86dd980f-3d30-32f8-949c-2f3142932cb1 | -5.87822 | -50.09633 | 2026-10-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9994c4d7-510c-3a2d-8e8c-f9176ef7b90b | -3.04618 | -53.94146 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 33d78b1f-8381-3b65-b417-9e5a9d86fc6b | -3.70485 | -61.32482 | 2026-10-08 04:46:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94cb01fa-4cdc-37e4-88a0-04ce1cb0084f | -6.22656 | -52.84381 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5ed62356-b4a4-3eea-a553-31da2dfa5365 | -8.22596 | -46.34812 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63003e51-78c3-352d-b2d6-933a8d52f4de | -3.16819 | -54.73422 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| be994768-a6a4-3a60-928a-62ed9cfe8e8d | -3.26857 | -54.05325 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aaf994cb-0db0-3030-ada9-5628c5b7583f | -2.93837 | -54.14298 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdb472cc-d53e-34a7-9ad8-4d391a0bfbdd | -3.2978 | -54.05633 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c0e7d47a-723a-34a8-abd2-dde74504dacc | -4.34343 | -55.1299 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a08e0b39-589a-346d-a0b7-12faea3a3079 | -11.63704 | -43.70305 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c988c3c9-71f2-3b9b-8aee-6c85a4f46e7c | -3.48132 | -50.09027 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5283e7a7-978c-3fb0-b6ee-ac5b28a8130a | -7.28198 | -46.80428 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7b8ece62-531a-3a00-b4dc-2c2c22d1d727 | -2.91458 | -54.1095 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 62c620df-f0ac-3cc4-aa5c-5cff1505b03c | -4.52714 | -54.98098 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a228627-a2a2-3f34-8c21-42c9d8494709 | -3.06209 | -54.21487 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97b81391-bd75-32bf-a717-10a9b22d1ab6 | -7.43839 | -63.53893 | 2026-10-08 04:46:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3dc6e296-acc4-32b0-bfe8-73351e656f13 | -2.47773 | -56.10118 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9bb93fd-b898-3867-aebe-b4ae4ecc754c | -3.51192 | -54.62933 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f5c5340d-7467-33ec-9d59-93b9d7965bd8 | -6.03936 | -51.72678 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a774ee8a-3975-3c4c-a10f-ce3add2044b5 | -3.96871 | -55.83871 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea55cef9-07a3-3027-aac0-141adeaf6299 | -2.86908 | -54.15686 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 403b15ff-ecf2-3d6a-be59-f84119befdf6 | -2.96886 | -57.763 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1778daf-03ce-3f81-b2f7-14397fbbe42d | -5.73746 | -45.16474 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5a8650ea-7730-33dc-9cc9-2d85ff219afd | -3.86242 | -56.00052 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e44dec0a-ed75-3d89-9f60-e81cd75407be | -3.32101 | -50.17752 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 933667b6-1ba1-3b8a-b167-112032b31f08 | -6.32787 | -43.3559 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a8f0529-3e07-3615-b1ae-42c157ae2cd9 | -3.28932 | -54.01673 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09164a47-c269-37d2-9462-39cb8a550a9f | -8.07838 | -55.28954 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 410dfbfe-2556-3453-871c-525e50c30f40 | -3.67896 | -55.94853 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cdc08b8-2bb0-357c-9fed-eda277fe6dd9 | -3.28921 | -54.08607 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3f3c0a0-cc89-3f8f-8973-6c8558fbdf12 | -3.09118 | -53.72721 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5d11f7b-0405-33d8-ab12-4e449dcfaa2b | -6.09982 | -53.49952 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 993b5975-3ee5-3c4b-a779-8e699cee654f | -2.99164 | -54.14226 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72a1b2c0-d329-366e-9de3-9ed2e96dcfe9 | -2.99964 | -54.04485 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da568c6c-ccb0-348d-863b-a024120a6023 | -5.97139 | -55.36843 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b7e1f46-9604-332e-b41d-85937169dd29 | -3.27935 | -53.81925 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22f232a0-33dc-3738-8106-557344c6382f | -3.55281 | -59.47587 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b30ea993-4e62-34e9-aa48-3ffc79a91fe4 | -3.04369 | -54.25785 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 2b692553-52e9-3521-a250-a94a1d7e2537 | -5.81175 | -52.75629 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a433937d-db0d-3b47-a181-e9574e8f22a6 | -6.33156 | -43.35119 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2ec02c34-26b0-3744-97fe-28162c3490df | -9.91843 | -44.80109 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc2316a3-22be-3905-92f6-2bab3da844b4 | -9.34382 | -54.51506 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0ac66d6-149d-3ee9-98ff-4a6a3edaa4f3 | -6.30503 | -43.34147 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 760dc4f5-d059-3c29-a728-ee39d750c1aa | -2.85663 | -59.11787 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6302ff73-70b9-311a-848e-77b5658200cc | -3.30039 | -54.01708 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae2f451c-6628-3a97-a6e0-d5a94bf490d6 | -2.5065 | -56.16596 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 7a78cab8-5332-30a2-afc1-b2f20b1c36ad | -3.29168 | -54.02449 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cbd8ee1-6d54-3b68-98c9-b0e1ffade54d | -3.35551 | -50.48151 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc0cb3be-8a54-3857-93d1-952bae1226f0 | -3.03925 | -54.26167 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 95c99068-307c-3827-97f0-1d9351069ded | -8.08586 | -55.31364 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 775cac87-08b5-3cbd-846f-49d1c39fe4fa | -2.85355 | -59.26791 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0ce0929-f18d-3482-a938-d8d7c4faeb21 | -3.53769 | -54.66172 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c2247944-5792-357c-936a-fd2407de8de0 | -8.21681 | -46.32438 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5660b1de-d834-3b34-90fd-073155eeba0d | -5.74155 | -45.15952 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 462e19d0-cb1d-34bf-a3d5-6b285555d67b | -2.51674 | -56.26178 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea72f3e8-2d7e-365b-8fdc-efc2fba2ab91 | -3.55992 | -50.28548 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56b590ea-2428-377e-9530-b087f14bb30c | -3.0628 | -54.21044 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 070f02cb-c590-3367-a849-172d7f609a98 | -3.14006 | -54.3587 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06cebdf6-1ced-354a-8e87-f98fe30ee3db | -3.54185 | -50.09254 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65cdc231-f451-3351-84c9-9e6af1041c97 | -3.02134 | -57.73574 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67d51aa1-dc85-3d0e-a629-331fb9df2460 | -11.22389 | -45.25636 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b216b37f-9888-3fd9-a24a-7796cf834868 | -3.05994 | -54.22815 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b69a9b84-5e52-3847-81c4-c921d1d4d948 | -3.09677 | -54.28408 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33ad707e-4920-393c-ac5e-85950a8329a3 | -3.11546 | -53.76845 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34999b80-a640-366b-a624-f3b2a9ba690f | -3.01805 | -54.04773 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 075f22c7-521d-3922-89bf-b38c66182a6c | -5.70134 | -53.48918 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b162b9eb-63ad-3c36-838a-1924c4d21a9d | -8.73462 | -45.16997 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e00b05bb-a4b5-3ce7-aea3-0979d7cec9ff | -8.99154 | -45.9165 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26934fdd-b789-32ff-b73d-4e11df71dd7a | -3.64367 | -54.51261 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaeb97d1-0d8d-3f22-9546-872fa82ff0df | -5.87318 | -53.48776 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1171980c-c433-3b5b-bc20-2d8f9e9af92d | -2.9851 | -54.06491 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35863fa5-2eb8-3c48-b0c2-b45f974ed684 | -8.25579 | -54.72991 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 607ecf52-4b0d-30b6-ad29-32e5a6ec69bc | -4.3404 | -43.79495 | 2026-10-08 04:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 24672b5e-8296-3ee9-9eed-301a2c032250 | -2.56806 | -56.15992 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f448bd3-ef10-35d6-a9e2-298b4e1f3a1b | -5.96378 | -55.34298 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c36c7440-691e-35ac-a551-a7a694b22454 | -2.50978 | -56.33141 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a9a44c7-a9fd-3ca9-b477-742087da4cde | -10.43207 | -47.28214 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e8c5d97-4e02-35fb-bb9c-748b54a2f819 | -4.07218 | -59.84969 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 544d1081-54e8-3e23-a17d-f8bb5a80bd4c | -5.1992 | -48.21362 | 2026-10-08 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c91277d0-b98f-3a03-965a-5831385a3fb6 | -3.07893 | -57.75213 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 947c13d9-4c22-3c20-80ec-9858a2033dce | -2.99018 | -54.05677 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 296d6616-b3c5-30d5-8fc8-baa8fb3f98fb | -3.01368 | -54.0515 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4858738-9385-36d8-8dc5-4df5d45107d5 | -3.84208 | -55.97088 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67b9ffb0-a0b1-3244-96bb-eb0acd2e9ef2 | -8.04626 | -49.83915 | 2026-10-08 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b657cf15-78ed-33f2-be73-918768fdc333 | -2.99845 | -54.07593 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 28a9ce65-c820-3957-b0ef-4a71ee11ae64 | -3.30881 | -54.05803 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c0b2c9b-c958-3079-a8c3-ca4ddb722052 | -2.96072 | -54.16925 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73b5dc4f-461a-31d3-b151-4118b6b9f9f9 | -11.22362 | -45.2573 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9ce2084-3fc5-337b-aa93-f55315ea6b9a | -2.846 | -54.13492 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f22bd3a3-89a9-34e5-8f4e-7256f2ac4ea4 | -5.1135 | -47.11563 | 2026-10-08 04:46:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README104.md)
