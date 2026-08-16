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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c941de02-ba47-3bfa-b6cd-cbde8042713b | -11.80623 | -44.80718 | 2026-08-16 03:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 020e317c-bed3-3cca-a86c-532901be7935 | -8.94711 | -38.00128 | 2026-08-16 03:36:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0f37fe3f-374f-35d0-816f-538345a709b3 | -10.52965 | -44.84999 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db1b479f-4c4c-30cd-a1c8-b006d0ee5256 | -10.53672 | -44.85204 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d148b20c-0549-3d80-8409-994bd00c0cca | -7.25675 | -44.69711 | 2026-08-16 03:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b848f935-b911-33b7-af23-5f71a71c3711 | -12.64426 | -43.9 | 2026-08-16 03:36:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c93ef404-eb35-38cf-8afa-207d9748aa4d | -7.25427 | -44.69822 | 2026-08-16 03:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4f62486-a312-38e6-8e1d-f230a8499e3a | -7.27398 | -44.72272 | 2026-08-16 03:36:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ddc8bd3-b86a-3429-8e29-a54d5901829c | -11.90506 | -45.98516 | 2026-08-16 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6235824c-c9e2-3531-9a88-1bcf05f4feac | -11.8129 | -44.8086 | 2026-08-16 03:36:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6e24828-195b-3994-9310-fba4221e6f03 | -13.37746 | -41.34443 | 2026-08-16 03:36:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4c799c70-43fa-38be-a00b-4a73bcdfe184 | -10.52023 | -44.86149 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8c361a75-b9f1-3c26-a188-d8b9398b2508 | -11.43172 | -43.91546 | 2026-08-16 03:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d269b933-6bdc-3490-8395-5f1f53062dfa | -13.37655 | -41.34475 | 2026-08-16 03:36:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a76e4431-b4dc-317e-a02a-8f7c15d5ecc5 | -10.52306 | -44.84928 | 2026-08-16 03:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ad558ea2-67e8-3b2b-af9e-c45fa2778c07 | -14.92422 | -46.6191 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91dffaad-47a1-385b-b328-ff068ab64a88 | -18.8567 | -43.75995 | 2026-08-16 03:38:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a250fddb-e9ea-3db4-a33d-fa4b1b7fbebe | -20.34809 | -46.70378 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e80cb007-1ff3-35e9-9107-ff7aaf16d01d | -15.57582 | -42.37157 | 2026-08-16 03:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23373276-c601-38cd-aecd-f845b9ac8f50 | -15.04576 | -47.03173 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc41f008-8532-32c7-ab25-fa7acc669add | -18.31277 | -44.51235 | 2026-08-16 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6de088cd-436e-39d8-82e9-0a50db7329ec | -15.05657 | -47.01704 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bda3ddc3-7a75-30da-8f9b-573ca8d94295 | -14.93266 | -46.61416 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3f9548c-683f-3c11-bedd-9c8606a12d49 | -18.3186 | -44.51371 | 2026-08-16 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80236d0a-400c-35be-879d-f70b92522196 | -20.33663 | -46.72416 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc9f4271-c280-357e-b53a-5b1e7ec57aa8 | -15.0623 | -47.02481 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8af38dd6-2291-3bf6-9887-91fe063956a7 | -14.90863 | -46.62315 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 53f07927-b35c-3287-8813-870532bf35ba | -14.91698 | -46.61868 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31e0e0ca-5c20-3863-9a01-d90ad9ebae6d | -18.31746 | -44.51179 | 2026-08-16 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e3b5ff2-3e99-3675-b16a-e1909ce1a756 | -14.7567 | -40.85688 | 2026-08-16 03:38:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3bba4e56-39fc-35c8-80a2-49458fab2cfd | -14.89906 | -46.63303 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 48b8ed27-f201-3594-9aca-90f824dd39d5 | -15.57048 | -42.37022 | 2026-08-16 03:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ff666696-a795-3ede-89de-e6df1a11d113 | -20.34089 | -46.70723 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fabb3f4-97dd-315d-8d4d-d63b5ec726cc | -20.33557 | -46.72943 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02283d1b-9e91-3818-ac25-19bded843910 | -20.32922 | -46.72784 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 607f175d-b730-3877-b5b5-9e1b4feb5d74 | -15.03816 | -47.0407 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cf209689-7471-37c5-abe7-28f60f77c4d7 | -18.95779 | -47.32251 | 2026-08-16 03:38:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 647339ec-612c-328e-b2fd-2b6aa0c679b0 | -19.23177 | -46.79403 | 2026-08-16 03:38:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c06bde6d-3b88-3bca-9f38-31514f771958 | -20.33684 | -46.72412 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aced8a1b-cfec-33f7-91cb-3fce3705c909 | -14.92134 | -46.61796 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 755e469f-84c7-35f6-a06b-ecc01da1a62f | -19.67951 | -43.84139 | 2026-08-16 03:38:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec339bbb-dd68-3820-b201-d2cdf72e6ed2 | -15.06382 | -47.01805 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54a15a42-1b97-3f90-8372-8d766e44094e | -15.05089 | -47.01823 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 829e5fe1-889b-39cb-946f-9dc8af078b43 | -15.04177 | -47.02519 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84c7a48c-71e9-3b0f-8a2a-e1c5233e8f70 | -20.34058 | -46.70719 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 395ded51-74ff-333f-a5d6-251c685d8016 | -13.68988 | -46.25373 | 2026-08-16 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8df5ce45-ccaf-364f-811a-31f840856d0c | -18.31647 | -44.51619 | 2026-08-16 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7a101fd-d841-3671-b929-e3e03dc1ea4c | -20.34842 | -46.70387 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01acd3f2-2138-3fa0-86c9-5adbe967bb98 | -20.34702 | -46.70972 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b40ab7f8-185e-33bc-a651-f39031e93c89 | -14.90753 | -46.62803 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2399b3bc-c149-3507-9f72-b89c13a65f85 | -15.05824 | -47.01886 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a4e3ced-e8ba-352e-8053-4c2223605936 | -15.0654 | -47.02029 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1de1f461-11e6-3ce8-a156-2b1cf2e5aaea | -19.67414 | -43.83978 | 2026-08-16 03:38:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a19bc26-265f-3136-a356-4c6e4f98ecef | -14.75664 | -40.85823 | 2026-08-16 03:38:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c7e3ab6a-eb10-3ec4-9aa0-8dd572f787b8 | -18.30794 | -44.50646 | 2026-08-16 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8e883046-f198-3115-80ac-e113679dd9e4 | -15.56648 | -42.36238 | 2026-08-16 03:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5a49521-826d-3418-b381-b7d1268596bc | -13.44127 | -43.8432 | 2026-08-16 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| edb35a13-3410-3222-9fe2-d0ed0aa2fbe6 | -15.04917 | -47.02563 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7b74305-efcc-3f02-9e4a-7b696caebd88 | -14.92548 | -46.61347 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd91648d-0fe7-37b5-b4fc-4e2bc495e93f | -14.92987 | -46.61283 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c58e2a2-38b4-35c8-9ba1-2b4bcffd1ac3 | -15.05521 | -47.02304 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f8791b8-3f8d-30ac-a4f0-cfc983b03926 | -14.9039 | -46.64421 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 549719cc-2e6f-3b1d-a759-086e30419229 | -15.57187 | -42.36348 | 2026-08-16 03:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30225a2d-2992-3f8b-ae2e-3d587d4df0d6 | -18.30696 | -44.51094 | 2026-08-16 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8f56b789-eb95-3484-836f-384b219711d1 | -13.69138 | -46.24691 | 2026-08-16 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 453abe76-af91-3263-b25e-4d537202d858 | -15.06887 | -47.0289 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8624251-7080-39bb-83dc-3bba1285b99b | -18.31765 | -44.51805 | 2026-08-16 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abfa4405-77f2-344f-b379-2741041f91d1 | -18.31958 | -44.50919 | 2026-08-16 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3ce8e01-beee-3257-95e7-80381ec2c76d | -15.0477 | -47.02313 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79378fbb-dfd3-3abf-a428-447c0e30f6fb | -20.34672 | -46.70969 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ce595b8-4a8c-3eb1-926e-ad7b8fa35161 | -15.07095 | -47.01965 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6abde0f6-cc55-39eb-bcb0-9101b6b416c0 | -20.3354 | -46.72947 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aba61281-954f-3b78-8519-44f771eb4047 | -17.17376 | -46.11739 | 2026-08-16 03:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 398fc00a-daec-3400-854c-011e7f78300d | -20.32904 | -46.7279 | 2026-08-16 03:38:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3a2eece-74a1-3ee6-b768-11dbbcd85081 | -17.17509 | -46.11153 | 2026-08-16 03:38:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1981e01a-8ffe-3cb5-9880-8039a35d9c93 | -15.57117 | -42.36685 | 2026-08-16 03:38:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d6113ad-6f17-3bb4-90ad-5add19ea9f93 | -13.43921 | -43.85309 | 2026-08-16 03:38:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1df328f8-41bd-3547-b74d-a0d4eb56aa2d | -15.0636 | -47.02808 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3e8a128-c047-37d8-b785-fbae4b2407a5 | -15.04918 | -47.01659 | 2026-08-16 03:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9997630c-9f72-38da-a8c1-ef06b2c1e979 | -14.89757 | -46.63965 | 2026-08-16 03:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d5cc116-52b3-37f6-99ba-ccba507bb3b4 | -18.30211 | -44.50514 | 2026-08-16 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 559b47ad-634a-3ef5-836e-9f58863eae8e | -8.9601 | -60.5165 | 2026-08-16 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 183.8 |
| 2a806155-f993-3a47-ad81-ee8b32425e55 | -6.82 | -56.4551 | 2026-08-16 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ee3048a0-aa58-3ba8-bfa3-c11aa83729f8 | -8.96 | -60.5358 | 2026-08-16 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.2 |
| dadc0c8b-b603-3d96-8c10-a7a8d4ceb0e1 | -6.6193 | -59.0802 | 2026-08-16 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| a6624321-43b4-3ecd-8e35-4ab76fff21a7 | -8.9787 | -60.5156 | 2026-08-16 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 58f68c65-86ff-3655-a025-dda371604514 | -6.2949 | -43.6194 | 2026-08-16 03:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 806f0944-ec36-34ff-a26a-89d805b1ee9e | -8.9414 | -60.5367 | 2026-08-16 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c7d0012d-2aef-3d4a-bc33-932f5a142237 | -6.3137 | -43.6178 | 2026-08-16 03:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 2af837ea-2cb0-3321-985f-cc37cb6b893e | -6.8597 | -58.9738 | 2026-08-16 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3dc83113-f84c-3f60-97ce-b4875c30e983 | -8.9785 | -60.5349 | 2026-08-16 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 755fab1b-a266-3656-a9b9-cec4738b617c | -8.9415 | -60.5174 | 2026-08-16 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d17a1f90-f5ae-3446-b623-748d5e56e11b | -6.6194 | -59.0609 | 2026-08-16 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3c9e8de2-76a8-3684-a655-5b48f33004fb | -6.7123 | -58.9412 | 2026-08-16 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| e5e1f9ed-65b5-35bc-92c0-85fad9bc7b6e | -6.6938 | -58.942 | 2026-08-16 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ceb440af-17b9-39a1-9797-27cdba197839 | -8.4275 | -62.676 | 2026-08-16 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 95eaec55-6959-306f-853d-97dab7dbcbde | -6.8387 | -56.4344 | 2026-08-16 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b1345a10-433e-3a89-851f-08bc8c8b689b | -21.43452 | -45.18297 | 2026-08-16 03:40:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7bb8f818-35ff-35fd-b969-69d46267e72f | -21.43469 | -45.18576 | 2026-08-16 03:40:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4103f6b9-a6aa-36f3-ac58-8e85129faf67 | -21.43362 | -45.18699 | 2026-08-16 03:40:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |


[Clique aqui para ver as próximas entradas](README9.md)
