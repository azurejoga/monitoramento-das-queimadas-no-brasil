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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfb1f482-f8ce-3725-9574-375e3ae1aba2 | -3.83561 | -44.09845 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5b9cfb51-860a-3073-bec6-f1bd3a61a79c | -6.46158 | -43.68121 | 2025-09-16 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4d1627a-a91f-3f07-89c1-edc0d50f281d | -3.82031 | -44.10722 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2f8854a-4eef-36a5-9686-f3698b42d14d | -6.40853 | -43.33649 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc8d21a5-0cd2-35b8-ba37-04078ff11e5f | -6.10045 | -44.92377 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c9d4ecc-0553-331f-b05b-8834997bae1a | -7.27274 | -46.59459 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9fa940f-2d4d-33ae-87bc-8cccd1cacb87 | -7.4266 | -40.08107 | 2025-09-16 04:27:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 01a05d8b-9c40-39d5-bc89-433d1a0e6c15 | -7.0656 | -44.15735 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f526512-81ba-3652-ad68-40296a480797 | -6.44518 | -46.11456 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 182bfd64-46e7-30b1-8928-05158b083809 | -7.44162 | -45.83853 | 2025-09-16 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05bdbd98-ed63-3f04-a80e-642553af7d7b | -6.34538 | -43.15865 | 2025-09-16 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 96cd4cc4-5f8e-3c65-8a37-ad26e2ebac3e | -7.51433 | -44.71299 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ed7e10b-0f80-36dd-bf37-91a78413b283 | -6.6305 | -47.88557 | 2025-09-16 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b162a0c-6c4e-3717-a964-ee957736ee2c | -3.83788 | -44.10623 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82af9d85-020c-384c-8ef7-6348259cf26b | -5.53096 | -44.86578 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f20c9a7b-60fb-3be3-9f44-1aab9455674b | -6.97006 | -44.5375 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97ad60fd-e048-3aa0-94d6-f8785bc1e51c | -6.88281 | -46.06244 | 2025-09-16 04:27:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5aa21e8-4677-3084-a7e6-e650399644ec | -5.97131 | -45.83702 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a04df444-d2bf-3b2f-9819-3627a052d529 | -5.83323 | -45.27174 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d115e35-c431-3c0b-aa90-fd5ec5ad3b1c | -5.34543 | -44.82296 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a190a126-fcd0-3d8f-b615-893f92d3b73a | -6.16448 | -44.53315 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b22aade8-ad6b-3584-a967-b100a545a41e | -5.8041 | -45.69707 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9359f6c8-fd66-32ac-8d4c-ce13a851a7c6 | -6.17216 | -46.81652 | 2025-09-16 04:27:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98456907-c41e-3be1-b0d8-49cc0fcd55db | -6.1838 | -41.19742 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8a8e0686-1467-3c33-8b3f-0077eb586074 | -7.30227 | -43.92583 | 2025-09-16 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f5e2b5b-893c-3bab-995b-3550a0611b41 | -5.76438 | -43.97027 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e73ce1f8-04b9-3a20-9b38-b480b552e00f | -7.05343 | -44.16704 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad062ef2-e0b1-3b80-8eb4-68f149e52140 | -3.83392 | -44.10933 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d2d58b5-f138-3dcc-ae76-777c20321210 | -3.07796 | -48.81688 | 2025-09-16 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e8bf207-d304-3700-9e67-9ba20c6cd541 | -7.36253 | -44.29076 | 2025-09-16 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b120a36-e720-3ccd-bcec-590111db8e1c | -6.26663 | -43.47393 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c920c90-f15a-3a9e-9bed-a2e7d93d47ef | -5.99233 | -45.81182 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b36e0ffc-def7-3cf8-86b8-df10651163e9 | -5.66926 | -45.04714 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2aa4d4e-6812-32c7-aee6-e6d304ca2c6b | -7.42395 | -44.86937 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1c102bc-a910-31ec-b4d0-63532eb04779 | -7.08184 | -44.55328 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 293c969a-2a6d-3aab-a120-41e8a74edde2 | -5.95562 | -42.72938 | 2025-09-16 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a646927-34fb-3d21-b277-6b76787b8bae | -5.54915 | -44.9706 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 718a1585-2e9d-3ada-b18b-fa9f57d935b1 | -7.27939 | -46.59564 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afefc5c4-6e63-346c-99b3-c94ec2b51dbf | -4.00898 | -43.23352 | 2025-09-16 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bd729a2-a4ff-3daf-a484-f0bd1959e7e6 | -6.98541 | -44.77314 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cec5661-cd2b-3012-b2dd-acb11e698313 | -6.18888 | -41.19086 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81f80924-453e-3589-8324-7c2bce64dee0 | -5.64606 | -45.94993 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ab48920-ec33-3541-93d0-7d3767ae8d11 | -7.54707 | -43.99722 | 2025-09-16 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f260294b-b1e0-3283-8fab-30a6be683075 | -6.96563 | -44.45266 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14a69c5e-33cc-3b7a-9ba2-6d6555344e39 | -5.78661 | -43.94953 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 96aa56bf-2972-33a1-b354-273188cf513b | -5.56035 | -44.96507 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d670e9b-1130-38e4-a72e-32f75a077f1d | -5.77677 | -43.92076 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 687c6878-4824-3792-8958-d5361e273d11 | -6.07697 | -49.55134 | 2025-09-16 04:27:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0a0f07d-e3ed-3a2e-a128-427e0f8c29ac | -7.08296 | -44.54586 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c61849d-7538-3a4a-afe5-a1a57b9a20b8 | -5.67192 | -51.1421 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97da84ac-8259-3339-bce1-b715553d95c2 | -5.20841 | -45.18214 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b0d773ba-c228-3532-8845-0918f33f0317 | -5.79008 | -43.95006 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 7b1df7de-25d0-3c03-90ec-31b7c26abf0e | -6.17829 | -41.20786 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 55aa245a-02bf-369f-bd67-553988e41ce4 | -5.34936 | -44.81991 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aff1a05b-7362-3f62-a475-39743e37f2d5 | -5.46412 | -44.68692 | 2025-09-16 04:27:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b3a58e4-7416-3ab0-ab00-b1f9b955339c | -6.77122 | -44.71503 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ed70179-c252-36a2-8a64-8f4f38183e27 | -5.90004 | -45.73348 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50963c7f-7b74-3ba9-bf86-d73865411318 | -7.66142 | -44.47836 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f61f482f-2a13-3d44-bad4-eada78d52919 | -5.77735 | -43.91694 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 849ac8bf-e78b-333c-837e-707f8ddddc1e | -6.18447 | -41.19434 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ff75d779-bccd-373c-b258-32745dd558d2 | -6.44889 | -44.09063 | 2025-09-16 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8bd3a71-162a-312c-bd22-7837f269e113 | -6.16143 | -41.23742 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c23c2017-7a12-3b8a-b411-71a984c78be8 | -2.16085 | -46.39729 | 2025-09-16 04:27:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58b2d8e0-fa57-3f72-b7f9-a95494da05ff | -5.53825 | -42.66027 | 2025-09-16 04:27:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| feec2d90-2275-3955-bf3e-733a60cc3ece | -5.90046 | -49.10101 | 2025-09-16 04:27:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3a2a2dc-3dd2-34ea-b4f0-d29f62219188 | -6.46601 | -46.00392 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94a1d924-4b31-3896-9b9f-d774b5ab4659 | -7.27329 | -46.5911 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 84fed922-fbef-325c-b483-4678b46f3aea | -6.17466 | -45.14386 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 37a79e63-1258-3a7b-9bf5-9f599aacf7d4 | -6.44847 | -43.60203 | 2025-09-16 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a20b02c-8d98-30d4-a5e3-2dece2cdd56b | -5.05696 | -44.32133 | 2025-09-16 04:27:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63cd23f6-f494-39fd-836b-f087f01f4164 | -6.17907 | -45.11554 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7399746-bb26-3d29-8520-e942709e539c | -3.15552 | -49.48404 | 2025-09-16 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a4ed5c0-0029-3899-9a14-3ec6d7338ad2 | -7.67698 | -44.4924 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c50e81d-c026-305a-8fab-8fa27c5a6fa2 | -6.28788 | -44.09014 | 2025-09-16 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b21e23b9-ba25-36ed-be59-82a5cfed3fb5 | -5.98786 | -45.79685 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 041360c6-734a-303f-912e-ad2fdc1e3bcf | -3.82995 | -44.11243 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26e6f9fd-8fd4-37e4-bfe7-030b448f7dff | -5.77786 | -45.88522 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e21a229-cfd5-380b-9c25-cfefbd82d902 | -7.27497 | -46.60207 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2de5e249-4bb3-32d7-a9ed-900f3cbd82e4 | -5.53938 | -42.66167 | 2025-09-16 04:27:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| f7d52e2c-8fe3-3d07-ab9b-37efbcd6ca71 | -6.98404 | -44.57675 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fe03526-e807-3e15-beee-3f4fa0609dbc | -5.67 | -43.3188 | 2025-09-16 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e6f749d-2de6-3c87-b005-740195bd743b | -6.40792 | -43.34057 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f092c992-ec60-3302-b921-9d6bd4ff5f54 | -7.27662 | -46.59163 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6cfed13b-b213-358a-bf36-e2ea1b504ac5 | -7.1366 | -47.97361 | 2025-09-16 04:27:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba8dddc1-5be4-3799-8f18-7fc0d6de416f | -6.17015 | -44.49647 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49bc0893-9d76-31d6-82c3-ee07fba2ac86 | -5.66649 | -45.06482 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bf4cdef-835e-34f3-9d7b-a2cde7535950 | -7.66891 | -44.47569 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c763d8aa-14b8-3764-a66f-89538be99ce7 | -4.89788 | -49.92613 | 2025-09-16 04:27:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94adc951-ef06-3c62-8e78-4f2092d1bb69 | -4.15915 | -46.78997 | 2025-09-16 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 652a28a4-6441-33ac-82b4-d9089187852a | -5.90779 | -45.72758 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70dc2383-2c77-383f-b4b9-aeb541db7414 | -5.7563 | -46.62177 | 2025-09-16 04:27:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efbddd1d-d53b-3314-94d4-c0e75f19ffd4 | -7.6885 | -44.48646 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5247693a-5b39-3ec0-8b8c-7c8db40d6f0a | -5.75818 | -43.91877 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c5dbc29-2922-3d8b-8084-eecd17b98576 | -5.80612 | -44.86456 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f760982-9d11-367d-83f8-27a0982c87b2 | -5.66314 | -45.06429 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fa0e4171-6d95-36c5-9773-7b1e8f352e8d | -6.64997 | -44.71128 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db47be45-6add-3ecc-a4e2-b7d102fbd05f | -5.55196 | -44.97467 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86079c0d-de6e-3431-b171-64d477b0210d | -3.97202 | -43.23975 | 2025-09-16 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4148a83-a76c-3d0e-b128-28593e104d63 | -7.52232 | -44.72952 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b45959b-7596-3018-9e9d-896084647478 | -5.98517 | -45.83562 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README31.md)
