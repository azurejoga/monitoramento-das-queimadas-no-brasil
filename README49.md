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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64849fcc-406a-332d-a7fc-1d6c295a9a56 | -8.69219 | -44.03235 | 2025-09-26 11:57:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4cd83383-65b8-33a0-848f-3fda067d352b | -4.74059 | -43.61004 | 2025-09-26 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 514cbf4a-b8aa-3638-90b9-07806fbb376f | -7.68826 | -45.88356 | 2025-09-26 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2cfb8a0f-2eff-36eb-9a0a-868fbd0ed064 | -6.13246 | -42.55112 | 2025-09-26 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5e464aba-defc-3642-b707-20f0b9718dd7 | -5.64893 | -42.83019 | 2025-09-26 11:57:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 37b25d20-5f5e-3392-9c4e-3e9373d166d7 | -7.58644 | -47.29984 | 2025-09-26 11:57:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5b9493c7-649c-3737-ab71-96d669a2e195 | -8.52116 | -44.62807 | 2025-09-26 11:57:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1d5f3002-8e4f-30e6-9037-8c6e48edbdb7 | -3.49146 | -43.14781 | 2025-09-26 11:57:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9c3d0616-dd66-3710-9460-d44810364b01 | -5.93147 | -42.91692 | 2025-09-26 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| a5b51def-6b4f-3a3f-8bb1-5da1feac6c5d | -7.8347 | -44.57703 | 2025-09-26 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0b98f526-3f21-3892-a033-1b52faefc43d | -7.48527 | -43.89291 | 2025-09-26 11:57:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 699c7227-cec9-3ac2-853b-01e58c6a5905 | -7.67124 | -45.99669 | 2025-09-26 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| da28be3b-0813-3391-9fce-284e8137d09c | -3.44291 | -44.12247 | 2025-09-26 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 74956d9f-cc20-3f8d-960d-1a33df3c3615 | -5.31772 | -43.14223 | 2025-09-26 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 68a534c4-fa97-383d-b32c-03e46b8e5c8e | -5.73307 | -42.63473 | 2025-09-26 11:57:00 | TERRA_M-M | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 471dcbaf-b927-302a-bbcd-7f1e89b87369 | -6.42423 | -43.08089 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ddd1697a-ea24-36fe-9f6a-94cc783c28f9 | -6.42558 | -43.07169 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3b6da60b-1d46-33a7-9367-2ac286fa2abe | -6.89524 | -44.75431 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 5ac81335-e8f4-3043-b404-dab323f42394 | -5.74356 | -42.5627 | 2025-09-26 11:57:00 | TERRA_M-M | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 66cd0d24-d44a-30d3-a84e-a2c03189d454 | -5.77571 | -42.78613 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 19477468-d2ca-3fab-8aa3-ae7e97fed896 | -5.93853 | -42.93385 | 2025-09-26 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 37e37e33-1435-32c0-9fc9-b7378480d641 | -3.39616 | -41.63778 | 2025-09-26 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| ea39094b-a26c-3bf3-8763-aa5d031d3adc | -5.7463 | -44.96702 | 2025-09-26 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 4d4247c2-2a9c-3dc7-9547-d74f45343700 | -3.68273 | -42.39649 | 2025-09-26 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 48e95193-ead0-3066-af21-c3eceb552ed6 | -7.05444 | -46.42136 | 2025-09-26 11:57:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 1532ce09-4be7-396e-b369-bd64e86599e3 | -8.32232 | -46.21117 | 2025-09-26 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| bb2fed61-f96a-3cbc-9f84-8f8c5e100388 | -7.0003 | -42.80122 | 2025-09-26 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 862901ad-1b2f-306b-9334-26716d7eff1f | -7.79927 | -46.01567 | 2025-09-26 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3b2c8ad5-2b38-3753-af51-942dae480419 | -4.75142 | -43.60142 | 2025-09-26 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b353687d-bb2a-330f-9410-1c3455eef3cf | -5.04705 | -45.12806 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8a192ad9-d3ad-3e4a-99ac-f75a7d2e1e0f | -6.13075 | -43.95395 | 2025-09-26 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1db0a720-0b56-39d5-ac7e-01f6b874ecbc | -3.39744 | -41.62895 | 2025-09-26 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 785250c9-780e-3be2-89e3-9ed2f58d6c86 | -4.49233 | -41.46137 | 2025-09-26 11:57:00 | TERRA_M-M | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 00d2491d-026b-3f22-b59e-6838bddc9dd0 | -4.35861 | -43.01099 | 2025-09-26 11:57:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 8dd610e9-2c1f-3bd6-8d77-6ca3e37ca37a | -7.09601 | -38.69806 | 2025-09-26 11:57:00 | TERRA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| d9a06b55-70b9-3d65-a156-9c12ab643b59 | -6.98247 | -42.79866 | 2025-09-26 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 358179e3-2111-388a-ac52-3fafa9113150 | -5.47533 | -43.0722 | 2025-09-26 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e72daf8f-5000-3e14-b220-6cc0b16a4025 | -5.18768 | -35.83297 | 2025-09-26 11:57:00 | TERRA_M-M | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 8a475de0-fa97-316d-bec4-fa524b27d765 | -6.57689 | -45.09772 | 2025-09-26 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 0a5a6f58-7bdd-3109-b196-cee2ec708ab2 | -6.13086 | -43.44991 | 2025-09-26 11:57:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 83082564-12f6-30f1-99c1-7343cb635335 | -5.46763 | -43.06163 | 2025-09-26 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| df2d7bdf-08a8-32ba-ab38-f799db4dd8c1 | -4.74635 | -43.26562 | 2025-09-26 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1a0c089e-acf0-3dbe-8c3f-6f24b2c2ee55 | -7.18187 | -43.51244 | 2025-09-26 11:57:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| d22b12e3-0573-34e5-b9f0-f7c57c69d87a | -3.36612 | -44.78536 | 2025-09-26 11:57:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 97c86770-cde5-3547-98f3-8d87105af41b | -6.17477 | -43.0834 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d6696675-3924-39fe-9913-91f3b98b170f | -6.34698 | -43.3548 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c966b08f-00d1-3b37-84a4-56ae148c0487 | -7.49306 | -43.90388 | 2025-09-26 11:57:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e654b042-1a27-3582-826d-4e0e4966805c | -5.77437 | -42.79525 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 05d70eaf-59a0-35d1-b99e-d9f840fcaaf1 | -5.74277 | -44.99034 | 2025-09-26 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| dbdfdc3f-bcb8-3f6d-b6be-605161222ebc | -7.18325 | -43.50305 | 2025-09-26 11:57:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 42.1 |
| 90f30c37-183b-3711-9917-30d96882ab55 | -7.2693 | -42.97861 | 2025-09-26 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 608118b4-f610-3e28-b5d0-ec3b98d1a805 | -5.73802 | -44.95411 | 2025-09-26 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ea57ced7-a20a-305a-824b-3fd07718e84d | -6.99138 | -42.79995 | 2025-09-26 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 46.9 |
| 0cc19891-dbff-361a-9d05-d30c45f45e7a | -5.75957 | -42.8958 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| b69f89ec-3f02-3ca4-bc8d-28a6e6b23839 | -5.60358 | -39.52797 | 2025-09-26 11:57:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 37.6 |
| 41c8211a-bc64-32a5-8f4d-8e35351161cc | -6.08617 | -44.68014 | 2025-09-26 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 85b6bb91-c499-33f0-b9ac-13daade36891 | -5.53424 | -42.73299 | 2025-09-26 11:57:00 | TERRA_M-M | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| ad20702a-f040-306b-80d0-f9befcefdf9b | -6.69115 | -38.44503 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 10.6 |
| b0095907-9b06-3aff-accf-a8cb954bdba6 | -5.73453 | -44.97712 | 2025-09-26 11:57:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 48a4c551-1c4c-3fb2-acdb-9301a83bb956 | -7.83313 | -44.5874 | 2025-09-26 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e36b461a-af7f-30d6-b77c-e6f32484d669 | -5.63566 | -43.9235 | 2025-09-26 11:57:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 904d3180-b6e7-3952-9503-f01eee53616a | -7.63779 | -43.80321 | 2025-09-26 11:57:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 34a077d9-cee3-3bef-a521-1b85f854e4d4 | -3.68405 | -42.38739 | 2025-09-26 11:57:00 | TERRA_M-M | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| dc5b6fdf-55a3-3bab-a9d2-9da4e1c4534f | -6.05648 | -39.58042 | 2025-09-26 11:57:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| babd74ce-9d0c-3baa-b3b7-36af236e6fdb | -7.26653 | -44.51365 | 2025-09-26 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 60821709-287d-3f0d-be69-7530b22230c0 | -8.12951 | -42.38421 | 2025-09-26 11:57:00 | TERRA_M-M | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 95bbaed4-5cd1-340a-90a8-dc398ede307c | -6.17344 | -43.0926 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 1b0c3468-26cb-3629-ab31-27b7867ecb7f | -3.45269 | -44.12389 | 2025-09-26 11:57:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| b6e0b8e6-5788-36d1-9399-cf4c1a63fedb | -2.95382 | -40.86632 | 2025-09-26 11:57:00 | TERRA_M-M | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 1cdd9a4c-a344-3bc1-84eb-51efb0fd91b8 | -6.71395 | -42.74187 | 2025-09-26 11:57:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| c3c69174-b8a8-362b-b45e-f8d10cb0c14e | -5.79193 | -42.86298 | 2025-09-26 11:57:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 2eacd980-be04-3943-bc2a-2d72c7acc66a | -6.42799 | -43.55682 | 2025-09-26 11:57:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0298fae5-674f-30a2-a7d8-315fd4e2a1d4 | -11.4221 | -45.0025 | 2025-09-26 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 3d48efd2-8e53-3261-8f05-54ceb992d0fd | -12.5761 | -45.843 | 2025-09-26 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 68bfec55-3634-3828-92a8-baf59e09f35b | -11.6233 | -44.4398 | 2025-09-26 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5629067a-972a-3a25-bccc-7ca7d178b40e | -12.5568 | -45.8459 | 2025-09-26 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d290c846-83d4-37b3-925d-eba890d5e9f3 | -10.0062 | -44.1766 | 2025-09-26 12:00:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| d88af278-b4e5-368e-b59c-bba0ec8463ca | -11.4225 | -44.9794 | 2025-09-26 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| a64c6c0f-2eb2-30e4-bc48-941a4a956c8f | -10.00977 | -44.16427 | 2025-09-26 12:00:00 | TERRA_M-T | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4f0970bf-6f38-32d2-82eb-570da2032185 | -11.63096 | -44.43116 | 2025-09-26 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 50cba724-ab96-3c64-99d1-4a0ce350d355 | -11.65283 | -45.34053 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 707c0bd1-99cb-3437-a0d5-ac38645b3880 | -11.42626 | -45.00484 | 2025-09-26 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 9aab75ae-bdcb-371c-93c7-567e0b7411a2 | -10.93156 | -44.29572 | 2025-09-26 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1a1ff666-fb6b-3323-9c39-e280cc7f343d | -10.72217 | -42.18051 | 2025-09-26 12:00:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 9cf9080b-4656-35c3-b894-ce1e461f0bb3 | -11.62953 | -44.44066 | 2025-09-26 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 75bbe1d3-8f70-3e21-881e-e88016dd4290 | -13.29937 | -43.55696 | 2025-09-26 12:00:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9b3fefee-2235-379d-9804-fd01f56032b0 | -12.37653 | -47.17249 | 2025-09-26 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 91f778c3-18da-37f9-86ed-4bb0e96107d2 | -19.02475 | -46.43831 | 2025-09-26 12:00:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| cf4c483b-5c5e-3914-9904-99bf5fda340b | -12.8029 | -42.78394 | 2025-09-26 12:00:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c832c277-9854-3551-beea-6cb81b736c12 | -9.97547 | -46.70684 | 2025-09-26 12:00:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 0d0be0ab-0bf0-30c4-a52e-caa22debf03d | -13.25048 | -50.68415 | 2025-09-26 12:00:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| cc26edea-8198-3567-b5bb-e28dd5ce8c22 | -9.25488 | -46.56367 | 2025-09-26 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2476b698-5680-36c7-87c7-3f97b0f2cf7f | -12.48745 | -42.93118 | 2025-09-26 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 4ecff8b1-177a-3319-886b-ba464d6796dc | -10.28737 | -45.21923 | 2025-09-26 12:00:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 43924bcf-1c52-3dce-900d-46c82d80adc2 | -11.96479 | -40.0113 | 2025-09-26 12:00:00 | TERRA_M-T | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| ca05ee04-c10f-3a51-af7e-9fa5523c1903 | -10.42784 | -39.51095 | 2025-09-26 12:00:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 54ec99e7-4175-362f-bbe1-d99e99bcab45 | -19.03395 | -46.43985 | 2025-09-26 12:00:00 | TERRA_M-T | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f38a25e7-f431-35c0-801a-d1ede6c7c804 | -10.93297 | -44.28624 | 2025-09-26 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 53755fec-8b52-3a94-be2e-6c394f396c45 | -13.85208 | -45.60721 | 2025-09-26 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 88c50e9c-5b4c-3700-9ef2-1e72a4ae0beb | -15.59075 | -43.52288 | 2025-09-26 12:00:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |


[Clique aqui para ver as próximas entradas](README50.md)
