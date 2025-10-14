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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c906c06-ef1f-360f-a9fe-b224dcc54dd9 | -7.9237 | -44.12654 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 865070e2-0705-3910-acdf-30b0438f96d7 | -3.56417 | -43.5106 | 2025-10-14 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6666e9b4-867d-3c73-8681-926e3389a8b4 | -3.38414 | -50.28379 | 2025-10-14 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3853255c-6cae-3d66-a32a-5220064df9ea | -6.16143 | -43.75443 | 2025-10-14 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb0e3dfe-b14d-3f46-ba3b-016c4f21435b | -5.11821 | -45.49472 | 2025-10-14 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e457518-20b1-358a-bea1-7c1676014a1e | -6.58221 | -43.91827 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ae19be8d-bec8-358a-9a72-d67cfc0a03f5 | -4.67107 | -43.13839 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75385287-66fa-3ee6-8c49-f81750537523 | -3.09197 | -50.38039 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 094125cb-ef8f-3e11-830a-a075ee844573 | -7.94788 | -44.1239 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| a27ca3b5-89cd-396d-9897-7a31f5ace791 | -7.16609 | -42.19336 | 2025-10-14 04:04:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0e979155-db69-3d38-9bdf-e478a591f111 | -6.30262 | -42.99798 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fcf9cfe6-a9ef-3e7c-b3d0-10cd5a8694b6 | -7.93789 | -44.11044 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc296ee6-6ec2-3a8c-b58d-312304a64b22 | -7.53907 | -42.704 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b85c2937-87b6-39d8-bfa5-d2a795679fc7 | -5.49626 | -43.06715 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d92b2049-c9bc-365a-9af7-9c279afbc5b4 | -7.5544 | -42.69846 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 31b7ade0-285c-35c1-9262-a75b0fcebf46 | -3.13428 | -50.20681 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccd4c4d7-d43f-3a02-92a4-20a28584b413 | -5.90222 | -44.91867 | 2025-10-14 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8984bf1f-7962-35e5-b4de-30ea29c4b13f | -6.98741 | -47.08889 | 2025-10-14 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67081155-df03-30dd-b14e-eda08ebabf8e | -7.65116 | -42.56717 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 358747f0-bd42-355f-8d29-35cc6f012622 | -5.89986 | -42.8363 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c580d2db-995b-37ff-ba05-95945f5a2055 | -5.78692 | -43.8955 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 844070cc-eefe-369e-bf07-5df6a257d8bf | -6.29318 | -42.98799 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b562c802-507b-3884-a45a-818164e55d9d | -5.90277 | -42.84103 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1268b544-20fb-3805-9e31-423a1b44c099 | -7.53335 | -42.695 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f5193361-ba63-3572-a5b7-3ee2e20dd241 | -4.80014 | -45.33643 | 2025-10-14 04:04:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1589ab23-2a23-374f-8d41-809e53fe6d4c | -5.48632 | -44.99728 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b140df5-3d23-3db6-9425-0dbbcb72e8e9 | -5.72065 | -44.53996 | 2025-10-14 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dec1265-f247-3512-af5b-80fcf83ff124 | -2.87494 | -50.7323 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46555582-7df2-3ea7-9677-73311a74c1f2 | -7.64768 | -42.5666 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 116716ba-46ab-3a97-b640-7f062ff252c1 | -2.88036 | -50.73827 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79be991b-8e0c-3893-a256-e4a0038c13bd | -6.33517 | -44.01732 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a471bb4-9a32-343f-b41b-d16dcaad3e42 | -7.9449 | -44.11876 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e3038aba-3b35-35d1-8109-f2d14df1b2cf | -5.30543 | -42.90902 | 2025-10-14 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6e898dab-b50f-3c3b-9cba-028e9914ed73 | -4.5326 | -47.40215 | 2025-10-14 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6508ac8-6c07-327d-802e-8dade2a8eb85 | -3.09808 | -50.38141 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce19fdf1-1be6-30c8-b618-5b347bc8008a | -3.06971 | -49.40931 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08db50b3-66d2-3a99-9503-e0f7b3556bcc | -7.50113 | -42.14563 | 2025-10-14 04:04:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b53ecdc5-92fe-38d0-9453-ed69afbd2e85 | -4.00363 | -43.27409 | 2025-10-14 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9173ba3-c3a1-3143-a914-c8d8d6ab605a | -3.05298 | -40.81454 | 2025-10-14 04:04:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dfc5fa3f-0825-399d-a252-86cde85e3672 | -7.69522 | -42.36927 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 52b9b886-ba06-3912-8003-26a15cc149e3 | -6.53791 | -43.56026 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3f14cff0-bb67-399f-b6ce-0f7532b24d00 | -1.95781 | -50.81371 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e7cf92c-e6cb-3453-a31b-3db9cda12f1c | -7.93943 | -44.12456 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 02feafc4-4256-3276-a4e7-7504a9eccb68 | -5.32888 | -45.19206 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6fc5c37-d578-3f6c-86cc-0b6449a560f1 | -5.21699 | -41.64869 | 2025-10-14 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5af7b2ef-5760-3a29-98d4-c8a85a2237c8 | -6.16066 | -43.75901 | 2025-10-14 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61bafd21-134a-3986-956b-19119af6e3b1 | -6.22358 | -41.56079 | 2025-10-14 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 675c36a2-ca36-3425-8cf3-c449a8d3ce16 | -6.43971 | -41.82499 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4b902d4c-9aeb-38c6-b65d-44230612bb89 | -3.13274 | -50.21564 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 379b4c94-1b50-39e1-9dec-a20e1d41d0bd | -7.90828 | -45.01228 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1ace52a-b1c2-3e08-807f-1cbb3210adf9 | -9.33071 | -40.88044 | 2025-10-14 04:04:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 25e43784-84db-3d96-b90b-dac1aa747fac | -5.5632 | -41.32181 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f3ad1581-bb69-333d-9506-663c8e7a9535 | -7.50187 | -43.06137 | 2025-10-14 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 86f1409a-14bc-3b2b-bca3-36cea8733de3 | -6.1929 | -42.59206 | 2025-10-14 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 12e599c9-827e-3dc2-96fa-0b0063727b2a | -5.65278 | -43.6072 | 2025-10-14 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 19ae5491-4412-3ea6-86dc-a29b7f677a50 | -5.8699 | -42.87869 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9e76b4ae-99ac-3fb6-b074-4eb304558814 | -9.16437 | -41.05882 | 2025-10-14 04:04:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e5bd1595-8ef7-3a38-8d6c-dd1b6b646ac0 | -5.42764 | -41.34161 | 2025-10-14 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0730431f-860f-395c-bc7f-ceedc514f967 | -6.85471 | -44.37063 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3aed556-9271-3fd3-ba80-b399f89c635e | -6.99791 | -41.99742 | 2025-10-14 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 38861445-e6ac-37ac-b0c7-20384f0d73de | -7.92222 | -44.13557 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 925f0517-bc44-3ea0-bf56-ee27c0ffd219 | -5.79912 | -43.89265 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 27654ff9-c1b9-35fc-8f94-d9473f970d67 | -3.1388 | -50.21656 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e32c370-26db-3569-bf42-dd2a30cc5f15 | -6.28599 | -42.98674 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e477d739-96f8-3829-95ec-be25dcb90268 | -5.30839 | -45.52519 | 2025-10-14 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 602bc662-3c9c-3684-88ae-bd024341b449 | -6.44091 | -41.81754 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ef46ed9-017a-30e7-bea3-bea9f6495bc7 | -7.94566 | -44.11428 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f58a0957-1d45-3ddf-b1ee-bda491d87130 | -7.84608 | -40.5605 | 2025-10-14 04:04:00 | NPP-375D | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 646401c6-8d94-3de3-a0fb-09d3ca25c0a7 | -5.59379 | -42.57482 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f502328e-3855-3da4-85dd-af277c034466 | -5.38752 | -43.22529 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e111ce30-382a-3cc2-948e-781b15427499 | -4.23169 | -43.01607 | 2025-10-14 04:04:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0727bc69-6ed2-39b6-86e7-f60b4632d3ea | -5.30611 | -42.90481 | 2025-10-14 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a4cf3b65-64c8-3317-b517-416578cff542 | -5.88227 | -42.87579 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a7f7178e-3855-3119-9382-0dbdb0a297eb | -3.36448 | -40.63665 | 2025-10-14 04:04:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3cf077ba-54fd-37ee-aa22-e5088cdf4403 | -7.16324 | -42.18903 | 2025-10-14 04:04:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5c8e9b33-ad97-34b7-8971-2240770c7e9a | -3.16735 | -48.60658 | 2025-10-14 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1503fb18-5ceb-3a4e-9a03-d70f37f25202 | -5.94463 | -43.73278 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ad392a9-f89b-33ba-b9b9-e3914377a1fa | -4.61911 | -45.7826 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4ded955-8520-36cc-9fb1-a76bc0ab9ddc | -4.23801 | -48.68791 | 2025-10-14 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82952188-9120-3b18-9e5c-65491ef2fa97 | -4.75993 | -40.86246 | 2025-10-14 04:04:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1c4d64ee-715b-3937-a421-522f40fdaf03 | -5.15368 | -39.50791 | 2025-10-14 04:04:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 91671670-3c94-3a3a-97c9-23ef2d4dbf50 | -3.90367 | -40.39068 | 2025-10-14 04:04:00 | NPP-375D | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dd11ce70-ad42-3b5a-ac58-478f86bc3ea3 | -3.15492 | -42.89165 | 2025-10-14 04:04:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7e086ec-c38e-32d1-b553-53ce5365d5a5 | -4.6153 | -49.54346 | 2025-10-14 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 761eb0a2-1c83-3467-a286-4be9c46a3b23 | -2.87953 | -50.74317 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5be7419d-19b2-3c96-9881-52c42ac4ad0e | -5.25969 | -43.21652 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04f0a6c7-9912-38af-8fc9-0258dace3990 | -4.37395 | -46.53618 | 2025-10-14 04:04:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5766680c-7d87-326a-a010-2a26915b39c4 | -5.87431 | -42.78229 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d5122608-0636-304b-bb1b-a168a2f61dd4 | -5.76308 | -47.9082 | 2025-10-14 04:04:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 961a16ef-fdd1-3060-9623-80395f8e38ff | -6.29677 | -42.98862 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a80bae0-2bb6-3ff9-a667-ab0ec6b5b5c2 | -6.33332 | -44.01911 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dde4f727-fed4-3a16-bb58-0c2bb822412f | -7.16825 | -39.23626 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4e86acc8-ab06-3f07-8aab-03e0f86ed3a4 | -4.69612 | -43.12457 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1ae921e-70a7-3b8c-835c-5614bd35c4e5 | -7.92519 | -44.11754 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9f2f2cfc-9c35-3610-83d0-85b41e7ac80b | -6.23603 | -44.90925 | 2025-10-14 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf34b126-90d4-303c-9ddd-1981103af73c | -6.23439 | -41.55878 | 2025-10-14 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| efc7f338-044f-3442-82d9-57bdeee66de5 | -7.90125 | -45.0059 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1ddd37b-65de-3471-b7b8-ce7078d54f82 | -7.15697 | -42.50085 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f12bd4a1-1133-324d-84dd-96ffb7e35cea | -5.74558 | -40.77118 | 2025-10-14 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b17eb640-9f69-39f4-8cee-f209f9593c2f | -6.15552 | -41.72374 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README14.md)
