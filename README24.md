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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37f9499d-6540-3ab7-b219-ed3df1ebd134 | -2.36649 | -50.34857 | 2026-09-30 04:32:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8b65494-b293-3ab3-a239-4222f2d70f29 | -7.17648 | -55.40904 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 663d47b2-9770-3bba-a4f3-fdce971c1210 | -6.20981 | -42.50938 | 2026-09-30 04:32:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a3c7b996-c698-3537-988b-b0a7598b6f74 | -8.84478 | -49.70536 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f5ec3199-0176-334d-bccc-7c78a643f7b3 | -4.30177 | -48.60711 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dfade4d-6154-3da9-bf88-97f6e40ab5fe | -3.09552 | -50.27308 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70097da6-aecb-38d3-94b1-4ac0d3822be5 | -2.18236 | -46.16602 | 2026-09-30 04:32:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b5e4721-1a6c-37b9-86b5-80731aa02d84 | -3.96366 | -49.01472 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d26c724-fbcd-35dd-b8e6-024545cd399b | -3.23877 | -46.93926 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 65a98d00-b5a8-3751-bd8d-cd5c88907245 | -2.90218 | -54.09283 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f8a05e70-9b4b-3688-88fc-1e0341b6a471 | -9.01018 | -40.99772 | 2026-09-30 04:32:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7335741f-25c9-357c-8145-f5a035745598 | -4.36497 | -47.77331 | 2026-09-30 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 982f58c3-7818-3c1a-9772-7a9bc827d6be | -5.73228 | -45.05587 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fa4d8c0-dba1-387d-9d09-8040fd63fd50 | -3.25089 | -50.81355 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a74e0524-1bb5-3383-a77a-98d0de032601 | -6.10501 | -55.70781 | 2026-09-30 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba7d774-97ca-3336-aabe-997b88d77297 | -3.23287 | -46.92988 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12c9874d-c192-3c86-bc4f-0e76107021ca | -6.3449 | -55.32866 | 2026-09-30 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ebbf521-68aa-3757-b9c4-127a0cf89ad6 | -6.13689 | -53.06255 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4c690b5-ff87-3db9-b8f1-31eb68e1d91b | -6.17892 | -53.28164 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a64795a-f884-306c-bb7a-95010334efd0 | -7.27099 | -44.312 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc0b898c-362e-3a7f-b126-267e6e4c9f21 | -9.04199 | -47.3299 | 2026-09-30 04:32:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7340d094-265b-3c39-96f7-0bc0c77d261a | -3.00969 | -53.87719 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 873b1df6-7644-343d-ad64-43e143de82ad | -5.98646 | -53.55226 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 377a2c08-f6d6-328f-aae6-18676c201faa | -3.26892 | -50.70189 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63438cd9-7e9b-35d3-ba10-6ba09c6b8eaa | -5.74721 | -45.17657 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5b31b87-c475-33ea-a29c-2f3907eef42c | -7.01983 | -44.6186 | 2026-09-30 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3d6f40e-413c-3532-82ae-48c01861f3d8 | -6.70833 | -45.63596 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b9cb2709-22d2-3147-b5b8-035c670deaf1 | -7.85097 | -45.8197 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fc06711a-80ce-31e9-b447-6bf61e31af37 | -5.81422 | -46.21735 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 178e7830-bdd1-3a5c-9a57-62be75090cf9 | -2.97798 | -51.02378 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8aaf9934-d745-3336-9f67-b8cd3378faf6 | -6.85912 | -40.93894 | 2026-09-30 04:32:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 119c212e-6273-3cf7-97bf-4a82e507368b | -5.81705 | -46.22157 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcf28592-1752-3593-91b1-b4b8e4b95bd5 | -6.112 | -55.70382 | 2026-09-30 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da8b104d-a332-3c59-a2a5-87f1893bf556 | -3.00452 | -54.22662 | 2026-09-30 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d363aae-2dcd-3459-8c66-8353db38a6ae | -3.03333 | -48.41012 | 2026-09-30 04:32:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0753392-58f4-30cc-aa9d-13c9d1d67297 | -3.56433 | -50.26008 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b01c44ab-e90d-3cd1-bd17-f7f65a390d92 | -7.53556 | -44.5438 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d226e8a8-5f65-3e07-892d-c0d4d09feca7 | -6.59966 | -43.91899 | 2026-09-30 04:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| de579328-1256-321e-8c45-9059a827e7f4 | -2.93083 | -48.75203 | 2026-09-30 04:32:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8df7cf18-a3e3-333b-8d70-a18b18f67e4a | -8.36376 | -44.17691 | 2026-09-30 04:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed893c0d-05bb-3c35-8b77-565ad74f7e31 | -7.07034 | -46.57141 | 2026-09-30 04:32:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dad770f5-6c39-38e8-a19a-cb87f54be3e1 | -5.73229 | -43.28372 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07158567-5ddf-3eb2-b296-4277523efeae | -6.71282 | -45.62947 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8c8111c-e660-3fc4-b10d-3d7d391d6b0b | -4.11576 | -48.81849 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e398288f-7428-3647-a12b-9d00f9f592a4 | -5.73497 | -45.16742 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 34ca656e-79b1-3a39-a70f-236e14d530d2 | -6.78315 | -46.46497 | 2026-09-30 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78432d74-18c2-31be-8e4d-de3aa71adac4 | -9.12951 | -44.74955 | 2026-09-30 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fac9d75a-5159-3d51-b51a-f3ec4f9a867c | -7.08172 | -41.74389 | 2026-09-30 04:32:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 86be4a6f-0432-3c70-9866-a7f61345c400 | -3.00939 | -54.22745 | 2026-09-30 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85355577-5e97-33ef-b43e-7e08ea9f02f2 | -4.81079 | -46.84663 | 2026-09-30 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04f14cf9-84e4-3c72-8bf8-ff053a311ba9 | -5.74109 | -45.172 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7ec621f-aa55-3c19-95c8-e968c68a90bd | -2.58052 | -50.79022 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc9e2877-f2ed-3eda-a2d9-8fb890cad02f | -6.3265 | -51.15762 | 2026-09-30 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 981c558b-4321-352e-81ee-8ad327780bb0 | -5.74229 | -45.05748 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ced22595-c10e-3149-b24c-328f30caff0f | -3.26817 | -50.70654 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f8c414b-d814-3ab0-92fb-9dc0507f6a5c | -3.22501 | -46.93277 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1c5e841-c34e-325e-95b5-cf6b134850ed | -2.38086 | -47.60333 | 2026-09-30 04:32:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9266b90-4878-30ed-aa63-d7c75541a025 | -6.72079 | -45.57999 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e51b478-e66a-3213-9e3c-688b1291cd75 | -3.18103 | -51.24594 | 2026-09-30 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 296182b6-53a0-30bb-95cf-d5be2566ae5a | -4.1244 | -46.87138 | 2026-09-30 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bffc0a92-4b4d-3b16-9aac-7cdfdedbd0f5 | -6.30361 | -46.06316 | 2026-09-30 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa5b6bb6-5543-355f-8bc3-a3a7877d11d4 | -5.73562 | -45.05641 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56a4f8c1-284d-3fdf-92e8-1260ca2de4f9 | -3.23884 | -46.9465 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 745c15ab-bb38-39a3-ad36-c84c0d1a9e0e | -7.02316 | -44.61913 | 2026-09-30 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76832492-02c3-374a-a898-0c301f705852 | -8.36743 | -45.39496 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8b9476a-cd20-3039-aec5-7acc95c9e9a9 | -2.97956 | -51.01405 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6e31902-63ae-3098-b7e5-6215b9bdeb73 | -2.73775 | -49.41873 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66083a9d-102a-39e9-92ee-a9658370dcbe | -3.24676 | -50.80538 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| efecf7f9-702f-3c6d-8dfc-42c6f5e6137d | -3.9648 | -48.12211 | 2026-09-30 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 863f7256-2c45-3146-a0eb-bf35d8ae5057 | -7.09961 | -46.4548 | 2026-09-30 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6b7b930-560e-34f7-b9d7-265e1c28b1d5 | -7.47212 | -45.79129 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f01c28df-d095-318b-8521-15c8c0f3aedd | -3.23747 | -46.94746 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c4fdb73b-5ff5-39f0-abc3-d39ed7024f7b | -5.74165 | -45.16849 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1ca7243-3faa-3eb7-be1f-289970708bbc | -7.51761 | -47.33204 | 2026-09-30 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ca9daf2-cb90-3abc-a004-2f543121bbf3 | -8.60689 | -49.45319 | 2026-09-30 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df6bba31-2884-3018-8a7b-3859157b57d5 | -2.97399 | -51.0483 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 581f10b7-94ba-366f-b771-c7f61d792c7f | -6.81937 | -45.05029 | 2026-09-30 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61ce27b8-07cf-3287-95f8-c561645bfed1 | -5.12971 | -56.01937 | 2026-09-30 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42b984b7-ca7d-37cf-91a5-87d658dd36b0 | -6.42824 | -46.66841 | 2026-09-30 04:32:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e5b119c-82d3-317b-9283-5eda518cdaca | -5.75223 | -45.16659 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee9c23e4-50ba-39cf-8475-d13b572501f5 | -7.43267 | -55.18148 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39e1a306-f398-3c40-a74e-d4fcbc533c79 | -3.23156 | -46.93809 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 14213660-90c9-315d-ba39-2ac4dad5a179 | -3.0286 | -48.4144 | 2026-09-30 04:32:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6c4eb6ee-f858-31e2-ba93-bb31b6429b90 | -4.36125 | -47.77271 | 2026-09-30 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5e29488b-ffe8-39c3-9652-75a8c572a8fa | -5.73107 | -45.1704 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| faef8578-488e-35e5-9bc4-4e3f3d9139a4 | -7.8504 | -45.82325 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 60746420-6264-3160-86c3-4afcbd892993 | -4.89864 | -45.48273 | 2026-09-30 04:32:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d2ba642-6063-3e18-a6a9-2799dd068d72 | -2.88532 | -54.87371 | 2026-09-30 04:32:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6835c65-54fe-3a37-91b9-2966b27806a6 | -7.26765 | -44.31147 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6f581fe-8456-3ce8-8c0f-0c86022907c7 | -7.9537 | -47.70883 | 2026-09-30 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 449ffdd4-069c-30ee-b359-0d77e770613b | -2.97559 | -51.03846 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a1fe1ab6-b178-3b69-b3a5-4083a503c5b1 | -3.23026 | -46.9463 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 478b9356-13f4-3ab4-b6de-c06d2a8986bc | -5.73285 | -43.28013 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b5a8e36-fb98-334b-aadb-bddec70dd8b6 | -7.81969 | -45.82198 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 983c5606-aa36-3826-b473-e0390fe8c68b | -6.13756 | -44.14751 | 2026-09-30 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05da5554-6169-34e8-a40d-0ddaefc61425 | -7.51643 | -44.54019 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3ed18d1-2573-3f0e-8534-c3c4a37c62e9 | -2.9725 | -51.0279 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 217e1232-ab9e-3072-a202-817dd0600fa1 | -3.22436 | -46.93686 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b86ea00-9bdb-3669-a5a5-319becdee314 | -3.23725 | -46.93363 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c58b26d9-3bd2-3eca-bcad-5c5828ca9947 | -3.3771 | -50.95015 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README25.md)
