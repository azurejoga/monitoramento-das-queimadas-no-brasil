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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7621ead-b96f-3e92-90f2-e2886ffcbcba | -10.43974 | -50.97778 | 2025-08-10 04:21:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cef83b1-d249-339d-a081-4e5731f06d92 | -6.6917 | -43.35471 | 2025-08-10 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 04034b45-380f-3079-8308-89c28e650eba | -8.05771 | -44.79278 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1e3d990-d4c6-3a75-b663-9245030c623d | -8.11084 | -47.44078 | 2025-08-10 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1404b5aa-bc4d-339a-b25c-3d67ee64b7d8 | -7.26898 | -45.36993 | 2025-08-10 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fde7854f-3890-3521-baf8-73802ad524b7 | -11.78011 | -44.94973 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 885d54c6-16f1-3595-95fc-4810794c9c95 | -7.41505 | -43.99338 | 2025-08-10 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57f8e4d8-f11d-3442-b7ef-2e7cbf5fadb4 | -7.40585 | -43.85472 | 2025-08-10 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9589761-5172-3304-8bae-cbccc583083e | -6.19075 | -45.44647 | 2025-08-10 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4774046f-808d-3527-9879-7d983a14ab93 | -7.89045 | -43.5419 | 2025-08-10 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7d22999-720a-3f60-8a5a-c9ee10a7912b | -7.71022 | -45.53367 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6acff033-86a1-31cb-a6ad-0d820fa5b493 | -5.43184 | -41.24405 | 2025-08-10 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d3963193-10d2-3870-838b-b21f1c0a46a0 | -7.73076 | -45.53344 | 2025-08-10 04:21:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64803bde-9905-32e3-b485-718a1196a6bc | -8.11277 | -47.42907 | 2025-08-10 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 120c62b2-ae14-33ce-a956-ebc56c543f46 | -7.32597 | -44.6908 | 2025-08-10 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8aa95e31-d94e-3a3c-a293-589bebfa9340 | -7.02735 | -43.54876 | 2025-08-10 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32a7d6b6-7cc7-3413-90c4-da7fbbae13cb | -8.98419 | -45.69524 | 2025-08-10 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3c17685-17fb-3ef7-b7e9-7aa688ceb794 | -7.4904 | -44.89155 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6b16c19-63a4-3f2a-b7e0-875659e9a227 | -10.4576 | -44.38699 | 2025-08-10 04:21:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 10b355a2-38e3-3dc0-b0aa-3cd15ea48f39 | -7.30094 | -39.64111 | 2025-08-10 04:21:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5fa95d36-ef35-376d-8c99-02a2615b5e00 | -6.432 | -43.53371 | 2025-08-10 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95b04de9-5e30-330d-b737-5b6cf70bf411 | -7.56228 | -45.41678 | 2025-08-10 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b154a7a-1a1a-34a1-a953-b79a38ae72da | -5.32 | -45.2578 | 2025-08-10 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f469ecb-0972-3e8c-a2eb-5d31b5ac2908 | -10.3584 | -46.62687 | 2025-08-10 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4850c342-5de7-3189-be6a-9d0b3f3693ef | -6.60846 | -43.39291 | 2025-08-10 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a51f41b-1eb7-39d9-9abc-c7e429a1d90c | -4.3015 | -48.07301 | 2025-08-10 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1f30836c-561f-3ff6-9623-cc53bedd11d7 | -8.88043 | -44.78776 | 2025-08-10 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cea32354-cdd9-3a0c-9c42-cb10c9263270 | -7.42951 | -43.98845 | 2025-08-10 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e205219-8ace-3d7c-8736-c098f8865a12 | -7.58532 | -44.39697 | 2025-08-10 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51e52dc4-2297-3769-8bee-71bdc0c32b43 | -8.11563 | -47.43353 | 2025-08-10 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d7cad870-dbef-38b3-a760-a4a0f7b48e47 | -10.34333 | -44.90406 | 2025-08-10 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 548d9574-6936-3540-b2ff-1ef42d58c8fe | -7.93061 | -46.81693 | 2025-08-10 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d683d97-22ab-3d18-b5dc-918bf9f64c0e | -7.32652 | -44.68732 | 2025-08-10 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ee6536b-58eb-37f4-b39c-29cef1e2255a | -5.32056 | -45.25429 | 2025-08-10 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7b838be-b06f-3be9-a144-f9cdeedfbfa5 | -6.9755 | -43.85995 | 2025-08-10 04:21:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 134c79a0-b201-3e53-b72d-61b90616caf0 | -7.31823 | -44.69669 | 2025-08-10 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 032c889e-579f-370e-a12e-de65ec9b0d8a | -7.88528 | -45.55847 | 2025-08-10 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf5efcc1-303e-3849-a18a-0ba976c90521 | -6.54248 | -47.43009 | 2025-08-10 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4eb1f21-64fe-3e1a-9cfb-cc99fdac93a1 | -7.2206 | -35.77332 | 2025-08-10 04:21:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1fed6120-9f2a-317f-962d-09ce3868044b | -9.86661 | -49.96637 | 2025-08-10 04:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 025f1485-5516-3c73-90d9-9e1b434e4a4a | -7.16274 | -44.06944 | 2025-08-10 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ad6da76-289a-3bf0-a5cc-041f6023397a | -8.50341 | -44.75647 | 2025-08-10 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2208e2f-674b-305e-9ecf-97cea69bfdde | -6.7304 | -46.30843 | 2025-08-10 04:21:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 699ed190-dc38-32c1-a851-4e8320776751 | -8.11148 | -47.43687 | 2025-08-10 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf3ed6ed-8ddd-3635-bb56-fe7cad9a7665 | -10.34 | -44.90354 | 2025-08-10 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b605e79-415d-3c5b-8e47-c49636d43614 | -13.5966 | -46.94273 | 2025-08-10 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee7dac79-52e1-3884-ba02-f5eb816cd604 | -16.37422 | -42.54133 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f160aa69-05f2-3663-918d-0adf2995e424 | -12.6882 | -48.20071 | 2025-08-10 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74d9e7b4-2caf-356d-908c-d399aa33570e | -12.57995 | -41.27954 | 2025-08-10 04:23:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 811c1f61-7732-3e86-9578-246564ff155b | -14.03459 | -46.34301 | 2025-08-10 04:23:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 038f5ea4-5ff8-3850-a77f-c5a30fdd68d7 | -13.615 | -46.93485 | 2025-08-10 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af4e22fe-8696-3cac-85f4-503b738c086b | -11.9227 | -44.86175 | 2025-08-10 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1fb338a-a0c4-33fa-8d3a-7d527868cc2e | -14.46714 | -47.84198 | 2025-08-10 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bff33246-9351-3aa6-a8f4-6f5f23eb1919 | -14.11021 | -45.40302 | 2025-08-10 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25850a54-12b5-3bdd-8e69-9c6eee75f126 | -12.39437 | -45.86813 | 2025-08-10 04:23:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34ae25e5-6f9d-353b-a8c7-40f55004ea90 | -13.61385 | -46.94197 | 2025-08-10 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f99251d7-727b-31ac-9ab0-b1e9d84ba655 | -13.04448 | -47.43433 | 2025-08-10 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97e35d82-b0b5-3a17-974f-251246c9b9ea | -12.59768 | -47.11329 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dced842-e243-3bac-b72f-8801276a3a27 | -14.28873 | -51.96318 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e46aac7-1dd4-3462-9584-7b9c14c11629 | -16.37563 | -42.53113 | 2025-08-10 04:23:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9087b34b-84b0-3ac5-bc98-2acbf6e5cab8 | -14.59147 | -47.16069 | 2025-08-10 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c95460a9-d4a2-305c-aae1-ec3db52e9765 | -12.64573 | -44.51302 | 2025-08-10 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b03f745-a60f-348e-ad23-dab7344c39d2 | -17.19536 | -42.82269 | 2025-08-10 04:23:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0b52fb6b-7ce1-3b83-aa70-70a95c86914f | -12.71465 | -46.36612 | 2025-08-10 04:23:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3c5702b-2127-3828-a9e5-cf42014e443e | -12.57527 | -41.28408 | 2025-08-10 04:23:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0b7c8ad2-28eb-3f1b-b280-714a4644bb14 | -14.11635 | -45.40772 | 2025-08-10 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd2df24b-0953-386e-a09d-6c2f2a8fbbc8 | -13.77799 | -48.87915 | 2025-08-10 04:23:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3571e28a-0178-3705-b4d0-ed27b564fb9c | -11.4281 | -50.59074 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2991dc5-faa1-33ef-b99f-60a91cef7746 | -13.60832 | -46.93377 | 2025-08-10 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 017351da-15ca-3d99-b0d1-e8172e696380 | -14.29977 | -51.97308 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b83947c6-d540-31c0-99c8-718b05422755 | -17.61032 | -46.70464 | 2025-08-10 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e360a92-0a62-3210-8e61-33e69035fdb9 | -15.05598 | -46.47443 | 2025-08-10 04:23:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0adae8da-292c-31f5-ab03-c2829e877123 | -15.15778 | -48.12738 | 2025-08-10 04:23:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bd81e84-873e-393c-a74c-41f3fefa8f01 | -14.29217 | -51.9678 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2be64df7-a6e6-3b7f-af70-ec062425f84b | -11.76445 | -47.48368 | 2025-08-10 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 489d5eac-c524-3e72-94a5-ee6c33cc6ac6 | -13.58537 | -44.89508 | 2025-08-10 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe278e92-9856-342d-a133-8a7f346be706 | -14.47053 | -47.84246 | 2025-08-10 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 480898f3-6a81-3373-ba78-c668da4c2ff0 | -11.93438 | -44.80841 | 2025-08-10 04:23:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6f76199-0be5-328c-901d-61fba2899100 | -12.60203 | -47.1289 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a91bdbc2-2dcf-3b6a-a54e-65c9c1c7a4a0 | -11.53847 | -50.55362 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91fde9d9-cb68-3585-a59b-3d352008c76b | -16.29801 | -52.92364 | 2025-08-10 04:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a2ea478-a736-3154-a19d-68d54a556ff3 | -12.55586 | -47.08417 | 2025-08-10 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e04245b2-cd79-3777-aa2b-9a2433727c9e | -14.29282 | -51.9878 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c0becf9-df7a-3cd1-aa81-295753a635ab | -17.57516 | -44.24617 | 2025-08-10 04:23:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9016ffa-54e3-3031-a030-542f4778468f | -13.64106 | -48.98533 | 2025-08-10 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 473c24e8-2f68-3b80-946e-14c076f0516e | -13.63338 | -48.98768 | 2025-08-10 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7751cb8-f07e-3944-b35e-2dd18e2c4ded | -14.0884 | -46.5779 | 2025-08-10 04:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09602eaa-3f01-3fad-a676-cb2239fd27e5 | -14.39773 | -43.78067 | 2025-08-10 04:23:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19080123-54a8-37a7-9208-94c8b29cad84 | -15.0962 | -46.53961 | 2025-08-10 04:23:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1397cfa3-a552-378c-b0e9-cf5a489ec3da | -13.11092 | -46.89524 | 2025-08-10 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ea399b8-287e-30b9-9296-db8bf1fe94aa | -11.10089 | -50.46158 | 2025-08-10 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 599869e6-87c6-3118-897b-20efd50315e0 | -14.11076 | -45.39941 | 2025-08-10 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fb617c0-31e5-3e3d-8198-f1873dbeff25 | -13.63067 | -49.0037 | 2025-08-10 04:23:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9626497a-a906-3d53-acae-436d820ba60d | -17.51509 | -41.73339 | 2025-08-10 04:23:00 | NPP-375D | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cbe8875b-4bba-30a1-8b39-e7153564c60e | -12.64912 | -44.51355 | 2025-08-10 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5d3b4f0-50f5-3110-85a5-3a4686488336 | -14.29631 | -51.96856 | 2025-08-10 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e9a9b557-e94a-3076-af65-81c95e709c6d | -13.05449 | -56.84848 | 2025-08-10 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4026885a-a9c8-386f-bb0e-0ba4394c9d77 | -12.16975 | -50.21943 | 2025-08-10 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c8467e8-aa1f-3366-9fa1-f04618378b31 | -14.45648 | -44.28734 | 2025-08-10 04:23:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62385d66-d28d-3d7f-9b2f-dbd39be10565 | -15.68906 | -43.21156 | 2025-08-10 04:23:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README17.md)
