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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dc56b62-f2b0-30fe-b05b-417e63a13b25 | -5.71817 | -41.6618 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 3da10790-6bcb-34a4-9410-23606d53e8da | -5.97331 | -40.91947 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| bf07e692-7c87-35b2-af26-2aae618e129d | -5.37251 | -44.17122 | 2026-10-07 16:03:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| e01927aa-11f2-3ece-b5dd-a9cc83dca1f3 | -4.11511 | -41.77813 | 2026-10-07 16:03:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c7c3484e-89d9-351d-b27c-ac269bffef01 | -5.02796 | -42.80363 | 2026-10-07 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c1b47f22-934c-39b0-9109-398e993e9f7c | -4.63017 | -48.85584 | 2026-10-07 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 683d22af-ada9-3163-9092-e2b0a6b2ef87 | -7.16784 | -47.79522 | 2026-10-07 16:03:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3ec5918e-5369-35ce-971c-399a10800fcd | -3.77366 | -41.77087 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 78b970e3-80e0-3d88-8d10-d5a78fab9785 | -7.21515 | -44.32729 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d8cbb78c-c9b8-323f-a87b-c44625303924 | -5.72183 | -41.66124 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 6056eca4-cb1d-334f-9954-80e6041c852a | -3.76771 | -41.78025 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 0bd85e6a-b1a7-32f4-a02b-3633d295e55e | -4.95339 | -49.16962 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 14b5d919-2473-353f-b925-626a513260b3 | -3.195 | -42.00853 | 2026-10-07 16:03:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3bd5520-06bd-37ee-81d4-7d270f4eefc7 | -3.91899 | -44.13869 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 66be1e21-0937-32df-b401-d184797903b9 | -7.87467 | -44.196 | 2026-10-07 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e5404746-a174-3a1a-9721-e93c7b5180bb | -7.46635 | -46.05218 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ad6eef5e-cd12-3a81-824b-06a2c1948c98 | -1.21771 | -49.03865 | 2026-10-07 16:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2be0d028-2543-3edd-99eb-ab1304e936ba | -4.33037 | -42.74957 | 2026-10-07 16:03:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88c5afef-7ab0-3c61-b835-773c831b0d38 | -3.76916 | -44.35133 | 2026-10-07 16:03:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 141.9 |
| d058bbc3-35b6-3a1b-a9c8-07409a0ef665 | -5.62006 | -46.67929 | 2026-10-07 16:03:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c7d8bfc0-f5a3-3c0c-9de1-e45371dc7205 | -3.76733 | -44.66081 | 2026-10-07 16:03:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 174ba4a5-caef-3082-ae61-ea8af3c102c4 | -1.67312 | -47.6609 | 2026-10-07 16:03:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 933ef4a3-04b8-30fa-a591-45e237785cf8 | -5.26196 | -47.93104 | 2026-10-07 16:03:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| fc974ad3-5932-3e7c-828e-9e7c385c6606 | -7.69642 | -44.74059 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b21e6fa7-a6e6-3912-937e-f15a91f4751c | -7.50719 | -44.4255 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a07d491b-8596-39dc-8a8c-c486ba3780b5 | -7.39873 | -45.64561 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| c8e53ff6-0dfa-3825-bcae-19ccf363d9a2 | -5.10159 | -42.92034 | 2026-10-07 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1242286d-03cc-3d25-8610-e492648ff32d | -4.82115 | -40.02102 | 2026-10-07 16:03:00 | NOAA-21 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 148.9 |
| 26412e17-371b-3584-b7d3-e732d47a1e19 | -7.47227 | -42.82568 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| c7c0dbc8-a0c4-3adc-9de8-4e51005896b4 | -3.5565 | -39.13971 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 4c4c08fe-0a1c-3894-89fe-78e24df8a76c | -5.72421 | -41.65209 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 87001631-d5ea-30ba-a667-3c72dc7e4f4e | -7.04843 | -44.32675 | 2026-10-07 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| fde45949-6b3d-387a-b7f4-31dd4ea92c00 | -6.95689 | -44.40995 | 2026-10-07 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eab4f574-3203-34fa-b9fd-adc84ec5db1e | -4.34661 | -43.79842 | 2026-10-07 16:03:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 596ac952-c22b-3333-b7c3-c906252ab9b8 | -3.36948 | -41.75219 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c2803e1d-3e9a-31d1-847c-7d1a4d4e4f67 | -7.0047 | -44.04702 | 2026-10-07 16:03:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6f8213fa-3eda-3d8c-b8d8-2bae4286f6e6 | -3.50057 | -41.94909 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 27a18e34-e064-399d-a36a-429c9fa12e4c | -6.92896 | -44.65187 | 2026-10-07 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c5a05178-768e-34de-9809-d587de9c323f | -2.94079 | -49.04011 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2cd689d3-7031-36d7-8f06-064a21797896 | -3.88481 | -44.10882 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1fcbb618-1390-3f22-8547-9df590911aa6 | -3.26189 | -50.40969 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| af3e633d-e4ad-3b28-8371-10107f70a3ea | -3.8837 | -44.10126 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9c063686-154e-3851-a531-3416c342e283 | -7.39231 | -46.22303 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 3116890c-ea01-3626-add6-902d2602dcc5 | -7.76306 | -43.81691 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 0d06c371-21b4-3e37-bfe4-5d54c4a934c7 | -3.94406 | -38.49409 | 2026-10-07 16:03:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 7dcf59fe-7468-3fe5-bc84-b7c444b88935 | -5.76905 | -38.56018 | 2026-10-07 16:03:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 135.2 |
| 52461593-6801-3bb9-8060-7acf550aa829 | -5.94991 | -46.40071 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 867a02f1-41bd-34e8-b389-799a3203cdea | -4.35631 | -38.85575 | 2026-10-07 16:03:00 | NOAA-21 | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9bea48f3-5cde-3bcd-bf49-ed6b30554ce4 | -3.86355 | -40.22644 | 2026-10-07 16:03:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 16dc9b15-95ac-308a-bd77-b835d5419fb1 | -6.64414 | -43.78642 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| aea25856-760e-3eb5-a45c-e1add3d5b898 | -4.26656 | -49.98782 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0abb7512-5a6e-3e29-b068-d3a0f8ed53e6 | -8.04649 | -45.6109 | 2026-10-07 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4d57408b-d907-3435-9373-e600026798e6 | -3.75063 | -41.71524 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 72a90bf9-19ca-3488-bef8-c8bd3db7c679 | -1.81937 | -47.85059 | 2026-10-07 16:03:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4d3e882a-880e-3526-b5a5-11fc97424b83 | -6.24291 | -44.34882 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3e3ff819-1dcb-377d-a0d0-db4973f52997 | -6.34724 | -42.57798 | 2026-10-07 16:03:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| a2b36e3b-e0bb-39c1-8c47-6a3f626b69f4 | -7.4058 | -45.6375 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| eda9fd03-4a6a-3045-bba7-2357fdebb25f | -7.24547 | -43.76535 | 2026-10-07 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 57cc4ecd-5bc8-3849-9375-4d330edd41f5 | -3.67744 | -45.12081 | 2026-10-07 16:03:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 466a4ba7-603c-3eb1-9e25-9a9d3ea0ca42 | -5.91095 | -44.06968 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f74a9e6a-b347-38ea-93b4-5c87d2afec6c | -7.73737 | -45.44957 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c50444b5-dce1-3fc9-aab0-078a95e8e5ef | -7.58857 | -46.69077 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8efd49a6-efe1-36eb-8e82-220ab8a3ae18 | -5.95629 | -43.87362 | 2026-10-07 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cf5ea21c-db39-3cb2-87ac-90a273b571ad | -4.09712 | -52.06792 | 2026-10-07 16:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| c6a8e275-4bc1-3a51-a8fd-16e9cbefc5fc | -5.72073 | -41.67908 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| e8522c9e-00da-3ac1-aea5-c099c293a3c7 | -5.74225 | -45.16722 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| debe9ab0-5156-3e7a-940c-d1d851284cea | -5.73631 | -45.15821 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 0956c4af-fce5-330c-a19a-fef2c598ecf5 | -4.77141 | -43.74469 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4028fb39-6f63-3065-a79f-7be12dfb3314 | -7.19682 | -44.29396 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| daea27cf-0a84-31b0-956d-f68a8d5eef78 | -5.62083 | -43.04877 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d37bc80d-f998-338f-83ec-63597c2db354 | -3.77255 | -41.78798 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 87ca5adb-3bdb-3a36-beaf-50f98cf44188 | -5.10304 | -42.93027 | 2026-10-07 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c0032bed-4768-3d03-9074-d7ab3db36754 | -6.29555 | -44.90806 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 3fb3df15-5502-3ff9-a0b3-70666426f89b | -3.47926 | -50.08694 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 0d0eab3c-6a88-3867-8ac9-b8c7d0bfa847 | -3.19106 | -50.56865 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8740f282-8708-3851-bf4b-5979d1acb5a3 | -3.80453 | -40.46302 | 2026-10-07 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 54412e07-c277-3e90-a401-35d29c11aacb | -3.94553 | -41.54229 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 60918901-a4b1-3c14-a1cf-a7e787974c93 | -7.54601 | -46.73262 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 791f19b8-54eb-3214-a81f-158b572acc40 | -6.69211 | -44.96102 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 074d3eda-c8c3-3530-af7c-34c466541e02 | -5.97627 | -40.91499 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| b88d57ca-ab28-399e-8487-598289276446 | -5.24409 | -50.92355 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a8400442-9121-337b-8df9-c06d0b74472a | -5.96128 | -46.37257 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 713a6f58-a0a8-37e7-a42a-11097dcca6b4 | -5.20642 | -48.34439 | 2026-10-07 16:03:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0f48a97b-3f43-3a42-a318-908f7880faa6 | -5.98211 | -40.9303 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 51bd67c2-4e3d-3df3-85db-e678fe7ef1a7 | -5.25701 | -47.93322 | 2026-10-07 16:03:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a500f2a3-9123-3fc9-aef1-11dabf617356 | -6.43726 | -44.84452 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| acb54606-5d5f-3bb7-a08e-989215231643 | -8.43611 | -49.87462 | 2026-10-07 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ef5685cf-f090-354a-97a9-3a915ebe63d9 | -3.1795 | -49.45558 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c824bb2a-f560-3599-9ca5-e44b82e54c6d | -7.40654 | -45.64305 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 689970d8-cc35-3c3c-badf-ad0eff99b7f5 | -3.48515 | -41.51328 | 2026-10-07 16:03:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e610f42a-c5f4-3b48-bfba-3a438a332542 | -3.20751 | -42.80204 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e011e39e-0d10-3717-86de-b86093707047 | -3.28463 | -39.67927 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 99e2d8c0-79cf-3953-8bfd-350410128c0e | -7.06663 | -45.36871 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 75a3d27d-deec-36cb-80ea-96476f19597b | -4.24033 | -49.98129 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 68d1490b-624a-3214-bfb9-b458be7bf095 | -3.94849 | -41.53772 | 2026-10-07 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 021448ca-bdfc-30d2-b21d-2832a16dfe27 | -3.18176 | -50.549 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1303d143-9594-3f43-a97f-207f34f368cc | -6.94967 | -45.3013 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5e995f04-4bf9-3ddc-a5cb-514614558317 | -3.36137 | -43.38881 | 2026-10-07 16:03:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 7496374c-a5fc-3a0b-8c48-8212df7d0117 | -7.09828 | -45.3178 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 19ab80c0-8693-3436-ae28-d547bd3d6d01 | -5.74754 | -45.17147 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README160.md)
