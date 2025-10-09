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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de75ba52-dcd8-37a3-8d39-75c38b4864a9 | -7.49945 | -42.73939 | 2025-10-09 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 331e04df-46a7-3686-bd32-665a064bb06b | -4.60957 | -43.15443 | 2025-10-09 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 307bf1bb-e8aa-3e49-acc1-5d8b30315628 | -4.25159 | -48.55573 | 2025-10-09 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1def1efa-34ac-3484-a172-44d0b4fa900f | -4.03495 | -49.49595 | 2025-10-09 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 540d5dcb-9b02-3bcc-95b0-484220d9e1fa | -6.57336 | -44.08239 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dba01876-0964-343d-bb40-8905743b7ef4 | -3.53772 | -48.92112 | 2025-10-09 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90eab53c-07ba-3ed4-8cbd-2a5d50541981 | -7.01676 | -42.87293 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6d57cd2e-8399-3898-8046-c9a068db9880 | -4.68434 | -45.84148 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e438070-ba4a-3d3c-ad34-bd9cb46dbea9 | -6.80215 | -45.62162 | 2025-10-09 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aae81449-bab3-3134-9392-86703b8f63cd | -4.76962 | -45.59788 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d53a23ff-4741-367f-b9b5-ac63ff81a5c0 | -3.44627 | -45.59996 | 2025-10-09 04:17:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9830b65-e9df-378b-99dd-fa4c3d65fb89 | -3.10627 | -47.79731 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c4e4fe73-6319-31ce-80ae-c44b53e1415b | -6.65732 | -41.99298 | 2025-10-09 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 636734a0-c2f0-3856-88b4-a14319195391 | -6.94852 | -42.70356 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0b52e74e-0709-3ba7-b530-7e313edff88a | 0.9061 | -51.12723 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 168f4eec-7a68-3d98-99fe-9582cfc4a428 | -3.26235 | -50.11972 | 2025-10-09 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dfcae1fc-0669-3775-878c-059a1b9dc0ed | -3.53426 | -48.91691 | 2025-10-09 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c7ebb08-ffe4-3ce5-bf51-2a6576b9b501 | -4.96836 | -45.6188 | 2025-10-09 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cec75fa0-849c-358d-aced-96c78866d0c3 | 0.88864 | -51.14804 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e33c9b1b-8fb7-32c4-b7d2-bb9d026c4f28 | -6.38339 | -43.86408 | 2025-10-09 04:17:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c9ca7497-c380-353c-a6b2-6dc9dc53fa7a | -7.48105 | -43.08943 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8a0ffe69-5619-3c7c-890d-92cb251d297e | -2.8984 | -48.07734 | 2025-10-09 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36cdec94-4f7c-3bab-b35b-6ff0b0c17230 | -6.45809 | -44.57824 | 2025-10-09 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0b5f4ba-2951-3ad9-b491-9cbc2a80731f | -5.48434 | -42.90434 | 2025-10-09 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eaf8c032-c6af-36e5-90f7-b00c62fe66f2 | -5.13062 | -46.25089 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65c3a98b-0191-3648-9ea0-92ed8ea54ac9 | -4.27056 | -48.8804 | 2025-10-09 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 615e0956-bd06-3cbc-bcc1-8e98debf67d2 | -6.7258 | -42.87732 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d681b57b-df65-3175-9d28-3ca730e915ef | -5.15236 | -46.09443 | 2025-10-09 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 234c1285-c4e9-3f7f-adf5-ae42d5cb709d | -7.45946 | -43.02587 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b7a2f718-4cf8-33d2-adc6-f8a0b272bf9b | -3.11067 | -47.79569 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9e7552ae-16b0-3864-ab2f-bcc29864b7fa | -6.92316 | -45.05305 | 2025-10-09 04:17:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 406c04e2-ca87-3950-866d-1f04c35da7f1 | -5.40235 | -40.9953 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| afea7d84-a3b0-35c4-bac8-58557cf0c664 | -6.39564 | -43.89444 | 2025-10-09 04:17:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a6438d1-c3f5-3eff-a793-e9f1151768e6 | -5.71566 | -42.76961 | 2025-10-09 04:17:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 045a799a-7322-39ab-8657-5473b87fc208 | -4.61011 | -43.15092 | 2025-10-09 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c46449cd-9cd5-3a3e-85e3-a4dd2668b622 | -7.0492 | -37.68981 | 2025-10-09 04:17:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| db0a4821-e6fc-3a3c-ab64-200712ed5311 | -6.72852 | -42.8139 | 2025-10-09 04:17:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 121038a9-1396-317d-b783-849e52b620f4 | -6.57462 | -44.16085 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e144aed7-de4f-3d45-9a0f-fa18a6d79dd2 | -3.96109 | -44.16906 | 2025-10-09 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed269f47-4b2e-3b42-ace6-c118ec288ff1 | -3.16741 | -48.70659 | 2025-10-09 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05e586d2-ae52-3be5-9932-6a885a05e899 | -6.90839 | -45.5733 | 2025-10-09 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e027b20-3d68-30cf-ab7b-84fc1828ebed | -4.81402 | -46.81893 | 2025-10-09 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7df4561f-1e0d-3efe-9e14-537eb207dfee | -5.24164 | -45.7982 | 2025-10-09 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fd8cdd9-9589-3dde-b0f9-f86f9575951a | -5.4329 | -44.46524 | 2025-10-09 04:17:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd2a12a5-55b2-3c3c-9abc-8d3bfdccd640 | -5.79609 | -44.66127 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d43eb459-2d2d-3b56-9487-412aa91c682c | -4.98533 | -45.12369 | 2025-10-09 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68a84a94-dedf-3e54-aaa9-af79dfc73991 | -5.6523 | -43.61044 | 2025-10-09 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fed194cd-16c7-3b20-af95-9fd16d695b58 | -4.51451 | -37.931 | 2025-10-09 04:17:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 91a100d5-3a7d-3056-8845-0af6b2041f9d | -3.67711 | -45.84641 | 2025-10-09 04:17:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82ccdbf6-1eba-3716-89ab-672d7c833a20 | -3.10994 | -47.8003 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 377d41d4-b116-38e6-93c0-905c51a934c9 | -5.04796 | -45.62756 | 2025-10-09 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6c1aa43-50a1-34cc-ad97-7c56b82b301e | -5.31491 | -45.38114 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98967048-a1d7-34ed-b0fb-fc01fb624ecf | -4.49309 | -46.35745 | 2025-10-09 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 68f76da3-02bd-33d8-b900-8324e2f033d5 | -5.64054 | -50.31619 | 2025-10-09 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 799446d1-4810-3615-a363-065015033479 | -3.10237 | -47.79908 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6cbcc35-f592-3b6a-afd6-5bab2c03202d | -5.39333 | -40.98115 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5c0f8c9d-d92c-37bc-a5ca-64c824ff93c5 | -5.73054 | -43.60832 | 2025-10-09 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28342b11-81ba-3a3a-af5c-043c253fe7e4 | -3.72042 | -42.84756 | 2025-10-09 04:17:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7551418-5a4c-3a75-8409-3a5d60a96432 | -4.89237 | -42.25137 | 2025-10-09 04:17:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54c76c92-9421-3080-8372-ceb274eea4e6 | -7.52578 | -42.72808 | 2025-10-09 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7fc22227-4172-331b-8c4d-4dfb7db279df | -6.69382 | -46.30022 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 41785e4a-4903-365d-a51a-bdbb89ad8069 | -7.52634 | -42.97604 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1e26083e-3f58-3620-bd71-ffb9999a0891 | -6.58556 | -44.1128 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af0ddf0a-66d0-3e97-940d-b63577c886e5 | -5.25663 | -43.14632 | 2025-10-09 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f05f306-652f-3c29-86f3-6470781e8d81 | -3.00421 | -49.7729 | 2025-10-09 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55204a9d-6dc1-3206-af19-2cd437e920d3 | -4.89949 | -41.52238 | 2025-10-09 04:17:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c73ac9d9-60e9-3f90-8e8b-55139e85e9ab | -3.83718 | -49.26144 | 2025-10-09 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b17ac724-0d24-3b3e-810b-45b9356ed864 | -7.52918 | -42.98023 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 82cd7bba-33c0-3348-90e9-bfc762e17a34 | -7.01571 | -42.744 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a3dcaa2b-236b-32e6-b86f-c456538b1de4 | -4.45586 | -43.22772 | 2025-10-09 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84c63d67-8bde-34fe-8e40-8f1fc729e73b | -7.05299 | -37.69239 | 2025-10-09 04:17:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 28be82a2-0afd-3770-9f72-2f1bf77843f3 | -4.73723 | -42.79728 | 2025-10-09 04:17:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a236a09f-75f4-392d-a878-876e4d3d2382 | -3.38984 | -50.13924 | 2025-10-09 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 530f58e1-c8eb-3578-b221-e5dc4c64f752 | 0.34155 | -50.95354 | 2025-10-09 04:17:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cc067196-9d0b-3703-a91e-038453a5d092 | -5.59197 | -44.87692 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd2c58b2-171b-37b1-8077-4c58fa41d583 | -5.80989 | -44.68116 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41543982-4498-3f08-b85a-9bd7e723a871 | -4.68153 | -45.83725 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31c6729e-8b23-324e-aae0-dbfeb4a8445a | 0.89693 | -51.1347 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be2ca83c-7643-35de-8014-5e8ae0ee8745 | -6.73481 | -42.84117 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 680272ac-c582-3b03-9f0d-baaca7ee62f1 | -4.25548 | -48.55642 | 2025-10-09 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe00d6d7-95f1-383a-9f49-88b47d594749 | -6.73084 | -42.84433 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1d6083b3-13a0-3f41-81e4-1b9d73ed2cfd | -7.01457 | -42.75143 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ddb34f2d-ada3-3f98-8390-8861b793cc0e | -6.68984 | -46.30332 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| a1d7b275-7b59-39c0-bfb2-1b272cee1a65 | 0.33524 | -50.95664 | 2025-10-09 04:17:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fcd34347-e933-3bd1-98b4-e37b429c0599 | -5.95304 | -44.72119 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 094d28b4-ceab-3ced-af06-ff070cf3ffd9 | -6.9244 | -44.50737 | 2025-10-09 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 362cdf87-47a7-33f0-abcd-2efefcf69a73 | -5.18884 | -44.93406 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2034d2c5-77ff-3097-8fa5-01f7d701b6bd | -6.72221 | -44.79753 | 2025-10-09 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bed219eb-7939-3e01-9c64-30777b959555 | -7.0538 | -37.69044 | 2025-10-09 04:17:00 | NOAA-20 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5451df91-d191-303d-9320-f3d6b9c25fce | -5.79554 | -44.66473 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 697c03c3-74f3-37cb-9a66-9ec9fe2bd019 | -6.56923 | -45.74039 | 2025-10-09 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed5cfb18-ac8f-3897-b4e0-54ee4ca31f7c | -5.12016 | -49.95621 | 2025-10-09 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b00e31c0-053f-38c5-934d-8ddc4dd4de27 | -5.15457 | -46.10244 | 2025-10-09 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90aa7cc6-c2d8-33d7-8b15-e95610e8da49 | -5.64565 | -43.60941 | 2025-10-09 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9931d3db-f913-31c9-9b90-e6d138832e6c | -3.38914 | -50.14341 | 2025-10-09 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8396826a-8628-39df-981f-b467a02cd15c | -5.27552 | -44.88039 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f7cf164-a1fe-3922-9e44-87c64e33d38d | -7.52521 | -42.98338 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b82e6abe-5367-3c2d-b199-739725e59086 | -5.76794 | -42.54549 | 2025-10-09 04:17:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5f5c47e1-65d5-3015-867f-31ac7b442123 | -5.43627 | -44.93773 | 2025-10-09 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e566e43-0914-3297-9ecd-8e0515ab920c | -7.25464 | -42.96854 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README33.md)
