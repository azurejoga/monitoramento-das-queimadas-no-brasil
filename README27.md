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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cdee81a-be90-33d8-bc5e-1b32c0388313 | -10.83234 | -46.14737 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9375fa64-f97c-3f5b-883c-730e01006916 | -8.2607 | -42.18009 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a04c05f4-82fa-35a5-9e8f-05d58c76b17c | -12.43306 | -48.48568 | 2026-09-17 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ee16661-97a8-3ffd-bf23-5ac1018e54c4 | -11.89279 | -47.585 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5ab8b8c7-2a95-324d-a572-96bde6d176ea | -9.51623 | -43.13853 | 2026-09-17 03:55:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 84cf0c08-62d6-331a-9883-e94784ff83c2 | -7.97272 | -44.83439 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27b7f212-6d77-394d-8d3d-c44fe6958aad | -11.2769 | -43.4878 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b6a745c-efd4-3700-ad3e-6fa04aeea92b | -8.61187 | -44.50542 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37008eff-1f62-3358-abd2-d9c643d331a1 | -7.00132 | -43.32877 | 2026-09-17 03:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f934655f-9213-3936-a033-4ce58d318e2a | -9.94735 | -45.30265 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc3e58b0-3b29-3377-89fb-64266b6faa9d | -9.86371 | -48.37109 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ff77a75e-0d6a-3952-b801-ac9bb46b5f8f | -8.56011 | -44.4801 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f99bbe3b-2b4a-3518-9a78-09d5f57ef763 | -12.44845 | -50.8496 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 69808a70-e9ce-392a-853b-449b25312a34 | -12.4615 | -50.91582 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fe3f998-e5c2-3e9f-bae4-63d0c273daa2 | -8.60972 | -44.49092 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a0d21dc-29e1-3002-97be-fa9803d202ee | -10.78231 | -46.19649 | 2026-09-17 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 69bdeda6-7b15-3e6a-b947-257702cb87b7 | -12.44319 | -50.8427 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd9dc9aa-f7f4-3fa5-92b8-fa5eff754bb3 | -11.88344 | -47.60438 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ea1cfb5-2896-38f6-b36d-2feb8c026792 | -14.13263 | -44.01231 | 2026-09-17 03:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f9e5e5f3-5bb1-3fa1-9415-f9379dcb7792 | -9.76955 | -46.09488 | 2026-09-17 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0f8fb6b-f4b9-37e1-a0a4-1c9fc22021e6 | -12.48497 | -50.93266 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2f354d7f-17a7-3819-8cb0-f9b89d37fc27 | -7.02916 | -42.07383 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 296b85ea-50f1-32d9-afe0-6007e7f0e2e2 | -11.53407 | -46.86267 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 156aa922-035d-3e65-9c46-1797bced1f3d | -11.52722 | -46.87086 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6985a7c2-16b9-3dce-85cf-a8a2a5e51ee5 | -9.87947 | -48.38301 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c41c5afc-91b5-3057-ad5d-4607c5b683a1 | -7.64516 | -44.32227 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecd730e2-6ae5-3c72-a3b7-9e0f306cf018 | -11.59012 | -46.87407 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8d8f3ed-e212-32bd-818b-c18d2b8de233 | -11.32332 | -46.77566 | 2026-09-17 03:55:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64f82edc-765a-3985-9f24-1b24cc0e3813 | -13.3073 | -43.71439 | 2026-09-17 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2552b764-53ac-3d81-b8dd-ac942638d718 | -12.45831 | -50.83463 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 8e1977e9-ae26-3519-9a69-8ceb562daaf6 | -10.50726 | -46.28851 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e0c5e1d-5332-3a28-be31-2fd033a5a2bd | -10.46191 | -44.94333 | 2026-09-17 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd8126e8-7c2c-3825-ad89-69b206212ea6 | -9.82983 | -48.35972 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a14f65f-1909-3f92-9319-eb354876c88c | -11.02157 | -47.57148 | 2026-09-17 03:55:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a71356c-457d-33e7-b61e-dd430a2d6b23 | -7.48102 | -42.10072 | 2026-09-17 03:55:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f7fbe44-5d01-37c7-ab6d-25cb10097209 | -12.48082 | -50.92014 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c465bf5-abe4-3092-9dea-75e888ba7464 | -9.31014 | -40.24914 | 2026-09-17 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8445cc77-0fd2-386b-82d1-ffc0618d5575 | -12.48473 | -50.7723 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4e64eb93-2c65-368f-b64c-ea4e48e96c03 | -10.50422 | -46.33371 | 2026-09-17 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e3090ec-aa68-3380-9cd4-9ea5e493beb6 | -11.55551 | -46.88928 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26cd8da0-0408-3467-802e-ae4910bf3521 | -12.46726 | -50.88824 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6429f4a6-4d8d-3578-94b4-47010fd31769 | -12.4684 | -50.88274 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6efa4678-192b-3e83-b064-f013736dd3df | -8.86174 | -44.90144 | 2026-09-17 03:55:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdbe9afc-071b-3c59-9d40-3708f48e3f9d | -7.10967 | -43.09524 | 2026-09-17 03:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7f480832-2417-35b0-b00b-f2b007ee4578 | -12.30351 | -47.42696 | 2026-09-17 03:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 325a661e-365b-35b0-9ec0-a018858f0303 | -7.10591 | -41.82419 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1756a725-c67e-3703-85ab-c25b5c5850ef | -8.10254 | -45.62599 | 2026-09-17 03:55:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b338e74-c602-398e-bcd8-c859240431a0 | -8.61226 | -44.47657 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 232df4fe-1329-39e0-92d0-4289d7508885 | -11.8877 | -47.59459 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| fdb7d8a3-2fb8-3d49-98a4-c7759b3ad10d | -12.44946 | -50.80992 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ded111f5-b0d2-31ef-8d23-928a19670c6a | -12.56753 | -47.09906 | 2026-09-17 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 695725a2-34c9-349d-961b-8fb3b7f9130b | -7.13554 | -42.16709 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2d3bd332-a77e-3808-91fd-f5079e0c6e8b | -12.44167 | -50.84819 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ac2a746-5d20-3f37-8ae0-ae787efa1251 | -12.44023 | -50.82491 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e6ea9f60-7150-305b-970f-74f9b3595caf | -9.48998 | -45.43018 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 3d309f8d-101f-3dd6-b2d1-cc9b95a7e750 | -11.34662 | -43.974 | 2026-09-17 03:55:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20c26a0c-2a7d-3b43-b57d-5825b52945a0 | -7.09457 | -41.84316 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b8d145d5-e3c8-3dad-a47f-5ef0dcd83a14 | -9.55817 | -46.60226 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78f7ae0d-1153-3d39-a50d-a05231a28ca2 | -7.94308 | -44.83206 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| eeb9b37a-b4a0-39ed-851a-32808362435c | -9.7808 | -46.48077 | 2026-09-17 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab06bece-d6ff-36e3-9e7b-9e1cc68e2156 | -7.72187 | -42.49971 | 2026-09-17 03:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| d5b1551f-caa4-3e71-bcd9-fb396b017f24 | -11.43587 | -41.4337 | 2026-09-17 03:55:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5d0379b2-e5a1-3cd0-8f71-9b9f3e42e2bf | -12.4319 | -50.86322 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d6235cd1-9f4e-35c5-b93f-bceb6aef94d2 | -7.97073 | -44.84192 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 79c95be7-c158-3c1d-b4e3-dc107259990d | -8.47238 | -44.90057 | 2026-09-17 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f9a7802-bddc-34b8-b447-03b628ae38b9 | -13.58315 | -45.47974 | 2026-09-17 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d4886d3-0148-3cdc-abbc-c5c11194b1b6 | -13.64899 | -43.74562 | 2026-09-17 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1234016f-69c7-3cb2-ad7f-5fafb01f4408 | -9.82629 | -46.50418 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6ec5b39-c99b-342b-b3b4-95e42a427c86 | -7.45544 | -46.16303 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79a2ef0f-ec7e-3e86-9a90-262dda692edd | -12.45168 | -50.79902 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 719f2b2a-6924-3636-965b-529dd31de7fd | -9.10873 | -45.72864 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 16a6cc56-ca60-32ac-a7ff-bf2afec16980 | -11.27334 | -43.4603 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b53d125-f49e-3f03-ad50-8586e7d6895a | -11.35438 | -44.0293 | 2026-09-17 03:55:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 853f8ce4-1d1d-3055-ab3e-0a927b2841ba | -12.47609 | -50.78168 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 37c32dab-85bb-33b6-a674-297f647ec22c | -8.25982 | -42.18526 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 93e18b76-7329-3c45-88ba-b00b3a377103 | -7.5997 | -46.32576 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57727de8-4460-3437-8ff8-56e4efb3e97a | -8.47396 | -44.69942 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44f9dce2-da50-391f-ae73-1ea8310b32a0 | -13.34066 | -43.78429 | 2026-09-17 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8873432d-71b2-3732-a1cb-b618389c792b | -9.83403 | -48.36913 | 2026-09-17 03:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 662784d1-2168-3461-80da-87aca8799556 | -10.60875 | -45.23375 | 2026-09-17 03:55:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6399448c-550b-3925-842a-b06022a3baed | -9.11861 | -45.7305 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 72c88c48-67b5-38c6-be29-8c36421b13a2 | -11.56182 | -46.88393 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb1f2fc4-0af1-3061-9095-c4b44547c6fd | -12.45278 | -50.79359 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 961781ca-83ca-3f78-8455-e794b3978cad | -12.50895 | -45.9286 | 2026-09-17 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6647e5d-27c3-33e2-80a3-d4f911d97812 | -12.48282 | -50.84579 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 4052c062-74f5-34df-b6bb-223e54830164 | -7.01525 | -43.3791 | 2026-09-17 03:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| abc545f1-8c29-3c1d-9a9a-e89182b11001 | -11.21299 | -42.82538 | 2026-09-17 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 336ddb7c-1b89-3af7-858f-f3374dea6ec0 | -12.46496 | -50.89926 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 92cb693c-385b-3dfa-8f8b-cc41f82ed532 | -12.48468 | -50.86913 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4edfbf5-ce5f-3f81-a0fe-bc413d41cda3 | -11.20207 | -42.81812 | 2026-09-17 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 552d99ff-4fe1-3135-8e98-b796cad268a8 | -7.04554 | -42.05809 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d5a0255-1c06-388b-be3b-8558a387ca7c | -10.30906 | -45.2648 | 2026-09-17 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e193bfe5-6d15-3d45-8a9e-623b78a9e92a | -7.09573 | -41.7652 | 2026-09-17 03:55:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5b0dd66f-a65e-359b-b26d-12b5290ebd88 | -11.27888 | -43.47663 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8e85ebc-e58f-30d4-aa56-917357b7a973 | -7.08024 | -42.09632 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 91e607a8-aa27-34ff-bdc6-b3e13763e06a | -8.60344 | -44.49962 | 2026-09-17 03:55:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba93d990-a457-3cd4-8723-9741a60fd12f | -12.46005 | -50.82373 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 727e4e76-f20e-35a0-96c7-cc6068d63209 | -12.45673 | -50.84013 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 6bbb250c-3284-39a9-823c-de3aed0640b9 | -9.61387 | -45.34682 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 07f8415c-854a-3a02-a3fc-5e2b7b5e6995 | -12.45365 | -50.82228 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |


[Clique aqui para ver as próximas entradas](README28.md)
