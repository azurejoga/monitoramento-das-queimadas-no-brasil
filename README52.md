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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f582035a-6cd3-3226-b8f6-4aafc16b805c | -7.25999 | -48.47951 | 2025-10-03 04:10:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c647c393-8484-3b5f-a40d-89d130bc72f2 | -7.18713 | -46.22213 | 2025-10-03 04:10:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a92a155-4f24-379a-be11-00619007e384 | -6.99728 | -42.31089 | 2025-10-03 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 19a33dcc-9303-3590-b8f6-3e2d2564997d | -7.30685 | -45.25964 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70c88962-3ea0-3d80-aae0-a9817af3d1a7 | -7.91126 | -43.53841 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a344fc85-3961-3047-8cd7-a4eb0ee365fb | -7.90903 | -43.53049 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2da39b55-8063-3cdf-a572-5b782eca94ba | -7.87198 | -47.30451 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c1d8876-efbc-33a8-9c50-5bdb2e721d63 | -5.50586 | -51.01738 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 591c9790-8b65-3f98-8df7-9dc5cefefdd9 | -6.28083 | -42.4277 | 2025-10-03 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b722063c-70f3-3aaf-91e2-fdc652ec3862 | -6.06569 | -43.21965 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6da56276-dd68-34f5-8c6e-59cd71d701c2 | -2.30385 | -48.14608 | 2025-10-03 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 675af839-61b4-301a-9fb7-eccad800490e | -6.32989 | -43.88322 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84327f64-3fb5-3f7b-bc22-ac83025ff473 | -4.65662 | -45.78577 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e868c83d-9687-34b1-a1d4-09a66158c073 | -7.76154 | -46.25914 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| cc1a7f2c-a0f6-386f-b4ed-98a3a7f7338e | -7.78989 | -47.37653 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8b8ce5f-fcfc-30fb-80fa-53bcb8a7dfca | -5.8285 | -46.36256 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9215049d-0c89-3111-ab42-59f9612a1ac0 | -7.79164 | -42.54582 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 796e5479-d8da-3889-8509-2bb75cae7dd9 | -7.76215 | -42.53751 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fb951008-6fcb-340f-b70e-4c9699eec3c4 | -4.48407 | -47.6783 | 2025-10-03 04:10:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 795d0129-e48d-3bda-840a-382167fc086e | -6.05174 | -44.61283 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0e71004-8ad1-3984-b259-179e4d2b5187 | -8.30367 | -44.85669 | 2025-10-03 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4037ee61-a122-32b8-a0b5-10eb0f6bfd08 | -5.95049 | -43.30776 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b763efad-12c4-3e47-9c93-d33c2ab133d3 | -7.31331 | -42.87194 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e912709-616a-3e8b-9990-aad40a96c7a7 | -7.25468 | -49.40904 | 2025-10-03 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 360831f9-b249-3ac0-90ab-f1ef1afd0d20 | -3.19563 | -51.02781 | 2025-10-03 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef3be126-506f-354c-b3d7-ead64430a06a | -7.87638 | -47.32861 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74be4b74-fa1a-31ba-b542-045b5951a13c | -6.4849 | -44.21991 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2613af30-5a6c-3c6a-a01a-d136b822d02a | -5.93725 | -42.88905 | 2025-10-03 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3f401c17-b77c-3f00-912a-64ceaf8bf66e | -3.84478 | -41.5824 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c2faf6a5-515c-3184-9ddc-5dbe486ecd92 | -7.06277 | -43.23455 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7e12dac6-b491-3028-9352-16a050dcb08c | -3.84422 | -41.58589 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3b4c2d77-b20e-3045-a1ea-8bb3cfd2baf7 | -7.75135 | -46.27233 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f83c1a27-f417-3db2-a7e9-03d7236d3d48 | -7.74948 | -44.79963 | 2025-10-03 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 159c7883-d1a7-3697-a292-ab3cdc949e8b | -4.42805 | -40.76204 | 2025-10-03 04:10:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c86f320-0576-364c-86d5-a04e57433a09 | -6.67351 | -42.78792 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 57fd1827-ffbe-3de9-9209-f46b51307766 | -6.99335 | -44.1983 | 2025-10-03 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 026bed8c-04e2-3cfd-b81f-8cd3bd23a0a5 | -7.30908 | -45.2689 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd658b5e-fea9-3589-8cee-52c0a39b186a | -5.75697 | -46.61492 | 2025-10-03 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| accaba34-7b17-34de-817a-882b9106e1a4 | -7.77607 | -47.38214 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 99374050-0c69-3956-b59b-e3141c9cb73a | -7.8028 | -42.51882 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e7d7319a-1a43-308e-b075-d271b84fc3c9 | -6.73215 | -39.11403 | 2025-10-03 04:10:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b9748649-e363-38f2-9ff6-ea38f601aa39 | -7.30612 | -45.26398 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a314986-6409-3930-b43a-dc95bc96033a | -6.04829 | -44.63384 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 933d6f3c-d317-3272-b164-1e3b4f309d3a | -6.11844 | -43.43356 | 2025-10-03 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f02810ed-9527-3393-89f6-a5d3f3208237 | -6.55891 | -43.89869 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bb135c6-298d-3494-80f2-0584c9c3721f | -5.94705 | -43.30721 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 52e7483e-dff6-390c-ba82-9dc988e54291 | -8.23167 | -39.0274 | 2025-10-03 04:10:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2972a64-7f63-3f61-9919-143fafd9930a | -7.83554 | -42.86031 | 2025-10-03 04:10:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bbc15654-320f-3094-b94b-070f570c25e7 | -5.79496 | -45.75356 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15391422-890e-3494-8035-4f0bef6dd6c0 | -4.66372 | -45.7918 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 6ae87976-e770-3e6e-8df6-91a7c297d3f0 | -7.55563 | -42.3962 | 2025-10-03 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 09ff8135-235e-374d-8b07-d4244d8303af | -7.75014 | -44.79562 | 2025-10-03 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9b644f6-2782-3dd5-9379-24f3efd38a79 | -7.75299 | -46.2625 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8028450f-c037-3f1a-9c98-6878c942ff8a | -7.55452 | -42.40322 | 2025-10-03 04:10:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e6ead56-e5d0-31ed-82b5-d8dfcc34cdc4 | -5.20594 | -42.72562 | 2025-10-03 04:10:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1bc1cc1-e96d-34ba-98db-67ce8402daee | -7.74767 | -46.2466 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e7c8718-5e8f-3d67-bd41-26bab72b4766 | -6.56069 | -43.88334 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51339bcd-6e88-3955-8170-2389b2995a3a | -6.33543 | -43.04125 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2c536ac-e9a0-3a20-99cb-6dfe48c59c6a | -7.75074 | -46.25211 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5c431e7f-30a7-34f1-8bba-3e9146bb53d4 | -7.90562 | -43.52991 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8388163-6fa2-3b88-84ef-b70e46a29dce | -4.65414 | -45.80066 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0b68ac15-780c-3532-8733-2b1e29c6de60 | -7.76593 | -42.59944 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3d49da97-da9b-3e7c-8f35-7986cd4fe379 | -7.88184 | -47.32162 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4990d148-8e11-3b7f-8d13-aba3b011d418 | -6.71221 | -42.80515 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 29b38dea-7f1b-30f8-89ae-94fe0951fde6 | -7.75846 | -46.25364 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| c277a60c-2fec-3881-965a-ce09acbc1f65 | -8.43933 | -46.80653 | 2025-10-03 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f9e38c5-8226-38f1-a8fb-a7e2b0f773b3 | -7.00664 | -47.18367 | 2025-10-03 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40e11a39-840d-3b08-81a0-576ff04a3ff8 | -6.7704 | -44.03902 | 2025-10-03 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99f62789-5bb5-3e10-840f-c12b50e0a8d0 | -7.94203 | -47.30196 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ac939e6-386a-3f85-a95a-4338d5de1afa | -6.41218 | -43.93171 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3b5e128-e8c4-3ea0-b5ba-ec8765b8d070 | -6.4512 | -43.12673 | 2025-10-03 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a08ab32-d0fc-3ed3-80d8-e5377dd06020 | -6.46146 | -44.20765 | 2025-10-03 04:10:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc1f87d2-c613-35de-b1bb-d95b120f0b42 | -7.05656 | -43.22982 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9fc05ff8-f7b1-3da0-81fa-78a4fedc5e2e | -4.04556 | -40.50637 | 2025-10-03 04:10:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4f811070-bd92-38f3-832f-fdc1d285aaa2 | -3.40421 | -46.90465 | 2025-10-03 04:10:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f9fde24-f31c-34e5-bf3a-50957e01cf3e | -4.65101 | -45.79512 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c1bd701a-63c1-391c-afc4-6c4a9c8a984f | -5.6209 | -51.94175 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf48e1b0-a842-36e0-9c43-45d15fcbceb9 | -11.43681 | -43.8814 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dc044f5-ec87-364b-9739-a17e9e7eaaf4 | -13.77532 | -47.53237 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 908591d9-49f6-3b00-b4a0-c6ef72115e44 | -11.04682 | -47.80899 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8ef14e9-89dc-323f-90b4-fc9669962fc4 | -10.91629 | -47.03759 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7a90bc3f-4b17-3406-8603-81b07ab8084c | -14.46778 | -48.4181 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08049473-5537-3266-bfab-bd6f827b599d | -13.75347 | -48.08081 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 40.5 |
| eb907ac7-d0ea-3844-ad31-d72963734d1c | -14.20085 | -46.10859 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7f5fa3ee-9e33-36a4-be54-7e57edfa5e7e | -10.16491 | -45.49625 | 2025-10-03 04:12:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5667d17d-895d-33d0-b8b7-60106d9df88c | -12.49871 | -48.00714 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 366e5528-1dbf-3344-b701-b264856c19aa | -12.3775 | -46.51003 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb203e98-6fef-34c3-b5ae-5c153d1ef39c | -13.77622 | -47.52729 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b2226bd-91fa-31a5-9484-dbc6d6948562 | -12.11426 | -44.20135 | 2025-10-03 04:12:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63da4562-4b1b-3691-b283-3cc2731907e5 | -13.63798 | -48.67691 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a21ca489-04f3-31d5-a386-bd4a325e2ff2 | -12.93934 | -48.4396 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 690a5664-c7cf-310d-a27b-2336ed588149 | -9.0618 | -46.64824 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af2842aa-4bb0-3ff6-a150-9366093e02bc | -9.9532 | -43.71789 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4d0d46d-36f2-3065-b967-72cc91273760 | -12.64557 | -46.99912 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1f01a2b-ee40-3cdd-b103-869bdf8e3b3b | -9.06571 | -46.64885 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ff639908-7a54-383b-8a6b-26abc3ddc60f | -11.05149 | -47.80624 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60c93123-e467-35ec-a0aa-ce0f0310aef1 | -12.63005 | -46.97881 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b7c8fb4f-20a8-3ca3-bd8c-914bacba72e4 | -14.19242 | -46.11532 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e09e8865-1205-3651-8043-95d28ccfe97a | -13.13763 | -47.89665 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca23934c-648f-316d-a99c-f5ba315a49cc | -11.42574 | -43.49268 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README53.md)
