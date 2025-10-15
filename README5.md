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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3d39dbf-a098-33c5-87e5-96f33b03f0e2 | -4.86469 | -45.54157 | 2025-10-15 00:35:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ccbaef34-29da-3e16-8cc6-8f4bd5a05e9c | -5.43311 | -40.99035 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 2ee802d3-3bf9-3dd7-82a5-1694c24d4c5a | -5.16585 | -45.16877 | 2025-10-15 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| a31d7bec-e00d-3302-9dbe-3cde273bf2d3 | -4.52264 | -48.05445 | 2025-10-15 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| fae48ca7-dfe7-3094-aaf9-fb3237d63fbf | -4.29527 | -45.50512 | 2025-10-15 00:35:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a93967a4-4d5c-3747-859d-851350befd9a | -2.04721 | -48.80383 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c65005e5-5b31-3fcf-bf19-8f53c864699f | -6.06175 | -41.90926 | 2025-10-15 00:35:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 566f63a2-b968-38f2-83a2-e6aca7b16f5e | -5.99391 | -44.08248 | 2025-10-15 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 7a05d401-65c2-33bd-8f15-aca0c951e666 | -3.16345 | -48.6109 | 2025-10-15 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 009734db-ba0d-3f55-baaa-c5509bb574a3 | -3.07468 | -49.49609 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f5c8295d-5888-3a41-a61a-defffaca0822 | -4.58995 | -43.55362 | 2025-10-15 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| df778984-ebbd-3270-af55-0b0b92ecb285 | -5.16347 | -45.16062 | 2025-10-15 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 8f615a07-415a-3bca-9346-aab83ee07c8a | -5.88918 | -43.74336 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 33e16da9-aa51-351c-9539-05e0b6d36bba | -8.46011 | -44.19476 | 2025-10-15 00:35:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| c7452d60-c548-3f23-84fb-5f99db2609a1 | -6.60638 | -43.622 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c7127096-cefe-3b18-801b-a918c0f32a5b | -4.87356 | -45.78189 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 69acc243-ba42-3122-b588-2ae418c23384 | -5.24391 | -45.61357 | 2025-10-15 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 38c12da2-de53-36a4-96b6-e009278e11b1 | -2.66448 | -49.52374 | 2025-10-15 00:35:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 871b29f3-4f72-3996-a750-e822fe48fa5c | -8.28828 | -43.44092 | 2025-10-15 00:35:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| de14a4dc-8f51-3cad-9413-01574298ce19 | -4.8622 | -45.54826 | 2025-10-15 00:35:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cbfaff50-9338-334d-b19a-526de3eeb6b4 | -5.31188 | -44.6058 | 2025-10-15 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d27fa90e-ec03-3a64-b709-15794d1238ae | -4.87227 | -45.66614 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 5fdf9349-05f1-35d9-8f13-24b50cc27b4e | -7.07734 | -41.95898 | 2025-10-15 00:35:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 5be4fbc8-7e7b-33e8-8062-1fec6d6c1dbd | -5.4868 | -45.41191 | 2025-10-15 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4061cd97-1489-30cd-b279-8a874e9d61b5 | -5.34612 | -45.38339 | 2025-10-15 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f01a58bf-42be-39a7-ae59-7b55a509f480 | -2.24529 | -47.86804 | 2025-10-15 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 3223db59-6d03-373f-b2e1-5007930b40db | -6.16296 | -44.38303 | 2025-10-15 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| ba62081e-b8be-31c7-94c6-6c3f709fb3d0 | -5.42862 | -40.98458 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 37.7 |
| c63a86a6-b5c0-3ce0-acdc-52850ffd9a49 | -4.41343 | -46.42819 | 2025-10-15 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4a37c81a-e259-3338-b3e8-df88bc21d131 | -8.2152 | -44.09316 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 73b298fc-ed99-3610-b2f9-4d11136bae2d | -4.64268 | -43.11826 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 2e1cca55-788b-36d8-a8ff-0574fe0aa7fb | -5.16364 | -45.15417 | 2025-10-15 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 229aa3d5-21bf-36ca-9fff-bcfbf3d49b19 | -4.87077 | -45.68597 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ae883e79-6c4d-3094-862f-4c66061963ec | -2.83532 | -48.83556 | 2025-10-15 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a8e5ba67-060f-369e-86ea-9d250fe63350 | -5.00862 | -44.50432 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 3d89f896-2b32-3af2-9e3a-aadfe7d6917b | -4.86673 | -45.5553 | 2025-10-15 00:35:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 91375641-4695-36c1-8f93-7714b98aa565 | -2.44844 | -49.37084 | 2025-10-15 00:35:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 85a5a56d-1fcb-37f7-9a7c-73b2faf2454e | -8.18496 | -44.04902 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 750115da-0bdd-3a44-a0e5-2edc2851a25c | -5.36963 | -44.75762 | 2025-10-15 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 223cb886-7e57-3dcc-a8e4-cc00fa22621b | -5.34128 | -43.74468 | 2025-10-15 00:35:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| fc6d88d3-9db8-3412-9ac3-123511cff57f | -4.28356 | -48.58283 | 2025-10-15 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| aa767a7e-4087-3ac9-b819-6c02907d032d | -5.24313 | -44.46724 | 2025-10-15 00:35:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| cb82e5ef-817f-3aed-8cf8-31e9c0ef36f7 | -5.97758 | -42.92868 | 2025-10-15 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| a8cd1e6d-43fc-3baa-acd0-1c9ae86d90bd | -4.77673 | -45.74802 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7ede0473-6487-3bb3-a6d3-a3fb496767e0 | -2.14511 | -47.60505 | 2025-10-15 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8a901f6e-fe49-33b0-a038-4d1d6dbd12e0 | -5.90835 | -42.83191 | 2025-10-15 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 96ee2213-379a-328e-9c8f-e63554bc68bb | -5.97446 | -46.60602 | 2025-10-15 00:35:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 21bed527-d89e-3089-9397-50f0aac05d53 | -5.14816 | -45.69485 | 2025-10-15 00:35:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 4a967d43-386c-380f-b51f-ccd24398c14b | -4.82701 | -45.90869 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0fbde288-0efc-3a53-9e2c-97cee1d4ccbb | -8.43037 | -46.24416 | 2025-10-15 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ee105f5d-c1d2-3665-b1e6-149befdf57b7 | -3.07716 | -49.51392 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| d64c8895-246d-3ca9-b943-be7b94a47df7 | -5.23849 | -45.60695 | 2025-10-15 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4e28c2d9-2c00-3fd5-a8c5-eb8e425615ae | -6.86903 | -40.81163 | 2025-10-15 00:35:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| f5d5bb85-6337-31dd-bdc9-6b47d644fe7a | -6.22776 | -44.17423 | 2025-10-15 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 7a4e94f5-c8ea-31fa-8791-671b87f2bb1a | -2.81331 | -49.20534 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| a07e5510-d135-3dde-959c-e2037007a38b | -2.66284 | -47.86914 | 2025-10-15 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b6cf14c5-bc5f-3cb8-a003-11cb2e15ff01 | -4.90394 | -43.46145 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 298.5 |
| eacea709-cda3-3bbb-b36b-a7738392ac96 | -8.22389 | -44.0861 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| fd86e7b2-7143-37ab-a8b7-ee18b1964956 | -5.33948 | -43.75166 | 2025-10-15 00:35:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2b91c29d-505b-32b8-9f35-41a20bca7576 | -5.31661 | -42.8993 | 2025-10-15 00:35:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 7bb2b78c-b2c1-326a-a0e6-40ed41c89f51 | -6.23389 | -44.16737 | 2025-10-15 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 9e3ae380-6b68-386e-8942-675e81ee2f2e | -3.13605 | -45.60964 | 2025-10-15 00:35:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| cac91a57-a24f-3887-adf8-662649cdbd95 | -7.93432 | -44.14033 | 2025-10-15 00:35:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 7ce23a75-376d-3b79-89fd-17d3f6d66e35 | -3.22618 | -48.92966 | 2025-10-15 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d51c6233-4f3e-3038-95e5-98df44862aa4 | -5.18476 | -46.1726 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 8d80b367-430c-3fdf-b956-b134c8fd3877 | -4.52127 | -48.04478 | 2025-10-15 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e5b5ed32-c10d-35dd-911e-2c5cff0f959d | -3.60379 | -48.99203 | 2025-10-15 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 96f4fc85-6e30-3ada-a236-1cf4575ca812 | -5.00561 | -45.8702 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 92af48fd-dfd5-3ce2-9bc6-9444e2273381 | -5.39114 | -45.44035 | 2025-10-15 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b7b05477-1991-3aa0-bf09-49a74da35594 | -7.08232 | -41.95154 | 2025-10-15 00:35:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 089ce7dc-424b-39a4-8def-a239daa1019c | -6.17402 | -44.29884 | 2025-10-15 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cbbbaa3f-0f63-3d01-bff9-4b15c2d37476 | -7.50338 | -46.63941 | 2025-10-15 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fe4dec8d-4b1d-3673-a833-30c6faf09cdd | -7.95684 | -44.14627 | 2025-10-15 00:35:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 40.3 |
| bb824c28-2d30-39ef-b093-288149fbbf62 | -5.42135 | -44.42836 | 2025-10-15 00:35:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5b221871-27d6-32c7-a0fb-9b821eee6266 | -4.87169 | -45.76887 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 22c71cc5-34f0-3ee5-b202-cb320b1dd0b7 | -5.82071 | -46.53674 | 2025-10-15 00:35:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| afec8094-c7e5-383c-81ab-3c41203fdeaf | -4.92204 | -45.38523 | 2025-10-15 00:35:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6f36f359-31d5-32ca-ba10-7c2ca320380b | -3.73547 | -44.15311 | 2025-10-15 00:35:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| dc619b90-6d7b-3f8d-b5f2-d25c9cfdb709 | -3.67525 | -45.20509 | 2025-10-15 00:35:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d982544f-f726-3df2-b1c8-e25961ff481d | -3.7846 | -49.4286 | 2025-10-15 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 1d3c129c-0036-319f-bcbc-703f56138789 | -4.65914 | -43.13765 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 7606ac25-91cd-35a2-b778-e4e3b01829ea | 1.33555 | -50.73677 | 2025-10-15 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 32f39d4c-e6fe-36b3-8c97-d73ea67f9652 | 1.31172 | -50.76342 | 2025-10-15 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4670e056-6b56-3fe0-9fd0-7b5eb118b090 | 1.30656 | -50.73579 | 2025-10-15 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 43db354f-7602-3f41-ad37-a71f113740b6 | 1.30778 | -50.72697 | 2025-10-15 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0aa8b5ac-c0b8-3db1-8145-2316c01972c8 | 1.80893 | -55.85632 | 2025-10-15 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 690dde43-0e67-3789-bb96-666fa8f4b34a | 1.81789 | -55.87195 | 2025-10-15 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a09a0d90-388f-3422-9ce1-a5257eaf9315 | 1.8805 | -55.66831 | 2025-10-15 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0e15565b-3191-357a-8201-b9af930cdc0f | 1.81993 | -55.85786 | 2025-10-15 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4c2d6f47-a980-380b-8cc9-fc87e11f5dfc | 1.31294 | -50.75463 | 2025-10-15 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4fbdda48-7fab-3af6-a7b4-446e5d9482ed | 1.32914 | -50.71791 | 2025-10-15 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 65e28ac8-0d52-3216-ba93-71693150812c | 1.30051 | -51.25023 | 2025-10-15 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9de66153-51d5-33b6-9015-332c0f58816a | -8.7404 | -43.8659 | 2025-10-15 00:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 9a9f2110-b6b5-3ff8-aae2-2a5e37565d43 | -11.0816 | -51.007 | 2025-10-15 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 57cfe899-f8ab-3eb0-9f04-fdc2b15893fe | -12.9183 | -47.0852 | 2025-10-15 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| dffe19aa-e750-3c66-96a5-4206ac58f262 | -4.6696 | -43.1326 | 2025-10-15 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 9a81e7cc-03de-3229-80b4-dadbc4d0b1c2 | -14.2424 | -51.6293 | 2025-10-15 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 1064aa2a-23c3-34ee-8c44-db8720ed135e | -11.0629 | -50.9877 | 2025-10-15 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f8c09816-96e3-3919-b4f3-7d01a30bfa0a | -5.8614 | -43.8627 | 2025-10-15 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 521d4fb6-25c6-31f7-ab9b-456d99866a7b | -4.6509 | -43.1337 | 2025-10-15 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 231.2 |


[Clique aqui para ver as próximas entradas](README6.md)
