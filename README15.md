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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70c9d556-4924-36f5-bac0-2b6525664378 | -7.19925 | -46.20165 | 2025-09-05 04:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d520cc8-b379-3b55-887b-567655bb3705 | -6.02204 | -43.70573 | 2025-09-05 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9d0b4f85-8241-329c-96ff-7cb73e7a0390 | -6.24304 | -43.29659 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9afb49e-857e-3dfa-a43b-dea5bae81c79 | -4.88646 | -41.76747 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e39a784d-9b56-3e02-837a-a5663f570893 | -2.55266 | -47.72448 | 2025-09-05 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4febe622-8d20-3fc9-8352-696ffca4488e | -6.69842 | -44.82672 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb3cda1b-0c87-3650-8fd3-33e0b50374f0 | -7.60684 | -46.21167 | 2025-09-05 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0a5a69f-b9bb-332d-a592-a344110c9805 | -5.60605 | -45.02342 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86bd39c9-bd0a-3923-963d-87a46087f225 | -5.95128 | -43.02545 | 2025-09-05 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8101a48c-063b-3f66-b0c0-7a58e9b74521 | -5.59839 | -45.02625 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f82470cf-0b93-3c73-b685-f26d9047ab84 | -4.89127 | -41.76424 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d1222aa9-f967-39e1-87c4-632a46eb2a49 | -5.70464 | -45.15389 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6bd418b6-9733-3230-a009-171b2c9c43cb | -4.89608 | -41.76094 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d52d7070-e64c-3f12-9eac-cb28f36d8dfc | -7.64587 | -44.75767 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f70d5672-92cc-3002-b557-5db11fb33807 | -6.34977 | -47.09738 | 2025-09-05 04:34:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c52e8c38-30eb-33f7-a522-75825f470d82 | -5.93514 | -44.15609 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d55e763b-9177-3aae-96e2-47818eacfea6 | -6.12367 | -44.11329 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8543a57-5e02-3034-abdc-29f6f1d41a51 | -5.55783 | -46.19112 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24466eae-5e1e-326e-988a-7034729533e7 | -6.78913 | -44.44822 | 2025-09-05 04:34:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d007b41e-0655-3590-8a19-002a2c74cab2 | -4.996 | -56.25497 | 2025-09-05 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c62422ec-b89d-3722-a964-37e2f06daefc | -6.16074 | -43.18244 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 077b41ad-ca8c-3b6e-aa8d-a1e2414611dd | -7.03837 | -43.26216 | 2025-09-05 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dff61f70-5949-3d36-adbb-49752ef890ee | -4.64553 | -43.12103 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8030fb22-e686-36a8-84da-964a4ad9572f | -5.54001 | -43.08841 | 2025-09-05 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 465b53fe-8ba3-353a-bf32-0a60654f6717 | -6.23867 | -42.64053 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 32c0f282-ec36-38e4-be73-bbef3eff019f | -7.42011 | -42.04164 | 2025-09-05 04:34:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce9fb74a-45a9-38d6-a803-57ced3e10b69 | -6.25307 | -43.28327 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6a783c07-abfa-337a-8f2d-1116e516b471 | -6.76749 | -44.46694 | 2025-09-05 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7d4d4306-bdf5-3fdc-b8a0-4caf56e82503 | -4.48858 | -47.67952 | 2025-09-05 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10f79d41-cf82-3775-b569-13c66b98a309 | -5.20428 | -43.69237 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f4f7c1f-1104-38c0-9650-c77c3f639be0 | -7.08423 | -43.86807 | 2025-09-05 04:34:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08756198-f5c1-35d3-b8c5-310bf7db7f96 | -5.75236 | -45.5456 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88f2eab7-50b3-33d7-82e5-f549c8719a43 | -3.68903 | -49.57103 | 2025-09-05 04:34:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6d2ed799-cce0-3a70-be6a-5fb468ac3485 | -6.27532 | -42.6462 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4764aa85-3502-3679-9ebf-46b1492f1d5a | -4.86269 | -42.54541 | 2025-09-05 04:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a0c32022-1766-3c36-8996-b0ee32cbf1df | -7.04921 | -42.36088 | 2025-09-05 04:34:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9c2b8bed-5c22-30b3-b4ad-1783ae0da786 | -4.23838 | -48.56062 | 2025-09-05 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23aa495f-a77d-3906-ab1a-b8e4fd7277d6 | -6.46985 | -43.67706 | 2025-09-05 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1f57413-0a8a-3ff4-b21b-52728c535af1 | -6.24173 | -42.64811 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0b10bc89-237e-31e1-be08-52f9afaa0342 | -5.47008 | -42.91747 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3e69037c-fe05-3230-9e67-b75ce49c4878 | -7.59256 | -46.21317 | 2025-09-05 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72ec666d-56bc-39da-8ddc-55a846418d0b | -2.44251 | -47.33338 | 2025-09-05 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c94ffce-8bb2-3d73-9134-ca7929f0a44e | -5.43263 | -42.85248 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 63ed5c8f-6dcf-3a70-8374-98da0b65a5b7 | -3.68333 | -49.02097 | 2025-09-05 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c58ee85f-ccc1-3f69-9467-a06e9b43fd81 | -5.29152 | -44.69984 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bd39172-f550-32a6-8954-123b6c6f9292 | -2.95063 | -51.66217 | 2025-09-05 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 173025f2-9449-3a29-892c-cb75c8b81a2f | -6.8959 | -45.18749 | 2025-09-05 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15ed02a5-7381-3196-aa3e-4ac2ee8cf968 | -5.54223 | -43.07338 | 2025-09-05 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87dfef15-5bb4-3eba-8083-2b773f597d48 | -6.59085 | -44.55271 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 46404e63-500b-3efb-99b5-08d36f9685f5 | -3.05675 | -40.84754 | 2025-09-05 04:34:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c3fcd2f-5de9-386f-b6b4-841b934c7025 | -5.20737 | -43.69525 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd0645ec-e280-3fb4-bada-532a970708b7 | -6.24379 | -43.2917 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cefd0fd8-3567-3e42-962b-697718b99167 | -6.72684 | -45.92046 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 9a2e8595-d1a4-3e0d-b433-275ace584747 | -5.63245 | -45.73482 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 907c3455-368c-32df-b81f-61c933e239aa | -7.35591 | -44.33311 | 2025-09-05 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16bf4ae8-89ff-3e31-b90d-356b8554b6fc | -2.44305 | -47.32992 | 2025-09-05 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15b77fa1-da80-3af2-b5ee-09d3169eee1d | -7.97509 | -44.52922 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cc2615e1-4612-31ff-9bcb-47ce4429a1a3 | -6.14412 | -44.84565 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2f7dea0-8d06-393e-bbd6-9e094f8c59df | -2.98096 | -47.37172 | 2025-09-05 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec97a2c3-8dc3-3975-b740-c93d36c41f27 | -6.12738 | -44.11391 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1ed19a3-4d94-3c4f-a24e-35817ba6e137 | -5.70044 | -45.18113 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00fe699c-4496-3957-8cd2-feec127eb94f | -5.97701 | -43.8254 | 2025-09-05 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 089a6100-b44a-3dad-866e-53944256caac | -7.07442 | -46.19463 | 2025-09-05 04:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23d83f58-8cc4-3bbd-8485-dedf4adf4f45 | -7.66669 | -46.70358 | 2025-09-05 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfe00560-2e0a-30ba-a10e-86ba3baef9db | -6.23459 | -42.64 | 2025-09-05 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1c9e2053-3bba-3f57-a4cd-857caeabf41d | -4.30764 | -48.07915 | 2025-09-05 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bcc1f010-6f41-30c7-8b80-c23ae7c57376 | -4.78877 | -43.81393 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9be086a5-b257-33ee-ae1b-0b17570cdb8b | -7.01827 | -43.23331 | 2025-09-05 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bbe6b0ba-2ada-36f1-baba-b8cbc4e51bbf | -7.64508 | -44.75952 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6134678-3ea0-3d37-9287-62e9c9bd349f | -5.4453 | -42.80978 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 61bdff77-09ab-35aa-b493-f6cc4085047b | -5.78496 | -44.91545 | 2025-09-05 04:34:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4e9b96f-e0ac-3092-93f0-e3338fd7e94f | -5.5352 | -50.89225 | 2025-09-05 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcd025c0-7662-30c9-bb47-ab0f5b3c2698 | -4.27596 | -48.19269 | 2025-09-05 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 324d8c6c-6abf-3c9c-85cb-f82a4826d96a | -5.69693 | -45.1806 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5d49dc1-7e33-389c-b8c3-07ecb5b2599f | -5.19981 | -43.69633 | 2025-09-05 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 518561f8-3f56-35da-991a-7bfa829e0ce5 | -4.17295 | -42.02778 | 2025-09-05 04:34:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0024dc4c-56d6-318a-8a8b-1c72e7d4ca60 | -5.63315 | -42.62419 | 2025-09-05 04:34:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ac4eb69-e8c4-331e-abe6-e030e5c636cb | -5.87253 | -46.03444 | 2025-09-05 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d57af9e2-f581-3f45-acfe-5f885c0cab26 | -6.06688 | -43.43338 | 2025-09-05 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 557d8506-665e-364a-80e1-bf58461a1711 | -3.02622 | -49.43072 | 2025-09-05 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3d88dbe-8a7e-3273-9e9b-1dc3951266ea | -4.89417 | -41.74458 | 2025-09-05 04:34:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 15ca147d-73c8-3d22-a235-4c08ca512983 | -7.97714 | -44.5156 | 2025-09-05 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb9341a6-c13e-3697-b774-b2aaac8f4903 | -2.51353 | -51.82362 | 2025-09-05 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12769f23-b1ea-3156-8f83-321523a96b0f | -6.73604 | -45.92936 | 2025-09-05 04:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fdb0181-c342-3d57-9706-53838b3ccc8a | -5.743 | -47.96018 | 2025-09-05 04:34:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44d16a39-4780-3b35-8e94-ff4388b1e350 | -6.24694 | -43.2972 | 2025-09-05 04:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15a098d8-1ae9-3fbf-98f3-2dce196cc75f | -6.32449 | -44.48998 | 2025-09-05 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b08bd477-8910-3440-b617-c7f74b022ea8 | -5.53656 | -46.43741 | 2025-09-05 04:34:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e942e4c-3c1f-3bf2-a423-b6c3d0379b2f | -6.37426 | -46.5545 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 479fb40d-81ff-381b-a660-49e51fea9f72 | -6.26618 | -45.08999 | 2025-09-05 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83b22dd7-b898-3bd5-92a2-db0133538bce | -6.11898 | -44.15499 | 2025-09-05 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 873396a9-d5ee-3944-a8d5-782738f60b83 | -5.34402 | -42.79206 | 2025-09-05 04:34:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b73d2de9-a79f-35a4-8da4-acdb71edc942 | -5.60665 | -45.01949 | 2025-09-05 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e20ea932-adc4-3df9-bbbf-812bf7193b78 | -6.27352 | -53.44445 | 2025-09-05 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d59cfb1-3ac8-326c-8547-7390420cecf3 | -4.85464 | -42.5443 | 2025-09-05 04:34:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6bdcd69f-72e4-373a-9e61-4fd4095bfc64 | -6.31425 | -47.7726 | 2025-09-05 04:34:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7965159-0613-3898-84cd-3d6b78008c79 | -6.00795 | -46.68786 | 2025-09-05 04:34:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8de34384-5c08-3fd0-a5fe-7ca15895c335 | -6.80755 | -45.36444 | 2025-09-05 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25295ddf-d531-3ead-885a-3a03a516edcb | -2.89949 | -51.48061 | 2025-09-05 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50d22f58-b584-3c16-82b5-bea33b48cbb6 | -7.60919 | -43.84859 | 2025-09-05 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README16.md)
