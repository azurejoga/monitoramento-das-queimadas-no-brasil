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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6db9bd99-47e0-3070-8ec2-f2d10c26f7cd | -6.32172 | -43.04176 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8c8338a0-44b1-3521-949b-9327026c1ce1 | -9.58121 | -47.0807 | 2025-10-02 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05d3816d-c944-3381-a07b-e8c3d8f45e67 | -7.56796 | -42.39688 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d60ab2d3-e14e-3c55-af2e-7d9ca17a6b62 | -11.7014 | -44.30415 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9db49818-d124-34ae-91ef-e74fe1bd2219 | -8.53161 | -44.68326 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7663ebf5-d3b5-3b4d-ae5f-e8f87e4272d6 | -9.39866 | -47.56873 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6014524-15bc-343e-872a-09d76aa75918 | -11.58323 | -47.65866 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 837d4e8d-0ea8-3503-8a2e-fd53e5f1ca48 | -8.8721 | -46.58376 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 527f783d-9497-3971-8465-1d0ee0827c19 | -6.72898 | -44.14906 | 2025-10-02 04:29:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a63ee9b-57cb-33bc-8059-2d894f501200 | -11.5956 | -47.23402 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54e82c8a-2c34-3a44-a6b5-455b176fd3e3 | -8.21082 | -43.59282 | 2025-10-02 04:29:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a54bbf9-ba0f-383c-a4d4-248c8598c52e | -8.88599 | -46.59648 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67b6dbef-e6ac-3fe2-85ab-4e7db457b8a5 | -6.26489 | -43.88915 | 2025-10-02 04:29:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62aee698-b195-3081-8981-e2a648d11d55 | -11.59727 | -47.22344 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b7355de-d5ce-334d-b4d0-2c63ab08cf8d | -6.32236 | -43.03756 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d8d25c2e-bc53-3c1a-bb33-3925166fdbbd | -11.27162 | -47.8359 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 699bb959-7455-3f73-a3e0-75c2d04aa93e | -9.94305 | -43.70225 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8807df01-b7f2-32f0-b1e8-a9c28b0ede39 | -10.88282 | -44.28394 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc2c7c9f-43db-3fc1-acfb-7f07dd8c7e52 | -11.44131 | -43.87727 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9281ad6c-af4b-35df-a01d-3d6ef31cc70a | -8.55813 | -44.64859 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be47cfb3-6358-3ad0-89d4-ba851016701d | -11.37876 | -45.04053 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db90be14-b804-3fdf-bfee-8227c2f3dc7a | -11.81158 | -45.00659 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 602887ed-98c8-3658-b076-1f43894fbb8f | -11.52467 | -47.17222 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aee95943-2c88-3949-ad4a-905e39e0dc52 | -10.78025 | -45.35074 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f0c56c9-8fbb-3d70-a5e1-37bcb9c05e0a | -10.82063 | -46.6105 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25b2f622-ef95-3d19-8b91-36f37e649e9b | -10.8301 | -46.61565 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 701f4f1f-969c-3618-95ed-6c80efceffcc | -7.7683 | -42.53968 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 0d999a94-5b41-38d8-9690-ff49860d685a | -11.596 | -47.64264 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2e757f3-43a5-3103-8ade-8ecf2b72611b | -11.05103 | -47.81842 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c397924f-f6f5-35dc-b3de-c249b680a911 | -11.27165 | -47.81414 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c979d5f0-cd74-394f-a665-bce23e80cd87 | -10.24928 | -50.32399 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd112bc8-d920-3857-be42-ae3d2f826357 | -11.17683 | -47.27517 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2b43ef76-0016-31ab-b3c3-1260cc2a1462 | -11.36127 | -44.93738 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c11fedc6-924f-38b2-be27-6d02684702d4 | -10.7837 | -45.35124 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b01c202d-954b-35f3-8c14-500cfd2f85eb | -8.55682 | -48.64583 | 2025-10-02 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b81d57d-5f0d-3e01-957b-9269486c36e9 | -8.51559 | -47.80072 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 914fbd9a-ccd1-3f4f-96d4-741c7917e858 | -12.75374 | -39.73929 | 2025-10-02 04:29:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 697a60a0-7079-3416-9b81-0575cb46e1c3 | -8.55742 | -48.64213 | 2025-10-02 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5293146-01c7-3f98-aadf-da34bf25b9b5 | -10.23843 | -50.32213 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 14f98929-cafe-3aff-b148-05f51942a348 | -8.88932 | -46.597 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffd47a24-193f-3711-907a-79dfee77be66 | -10.69845 | -48.58159 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d02937a3-3518-3a8f-a29d-d785159c9f84 | -10.99599 | -46.62001 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7e58941-8400-3532-8289-4f0a52ff54bd | -11.05938 | -47.80894 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77dcf907-845e-3ad7-93a6-7118cd9d1f1d | -10.66584 | -48.5689 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b47f52b-7e53-3469-a638-fa2d8a9d1218 | -11.75152 | -46.82717 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a05f1b3d-de07-3221-98e5-4113fa16caf8 | -10.35435 | -43.73492 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ee988a5-5c4f-376f-8eda-3c63892752ed | -6.38398 | -43.86577 | 2025-10-02 04:29:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a57d1e7c-d851-3895-a385-afee4a809bdb | -9.92818 | -43.72646 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| e8858e46-a7b6-3972-aa3e-d25507ebd3a6 | -9.93964 | -43.75017 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2fc4353e-1a78-389a-a67c-632e1b6c63ce | -6.54902 | -43.93762 | 2025-10-02 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d2fb6e6b-7031-397b-876f-d5100e5917c6 | -10.95538 | -46.66085 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27957255-a14b-3740-9ead-57a97f065da0 | -5.99703 | -44.59774 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b8c82e1-84a3-3cfc-9c98-1d40826e5342 | -10.96372 | -46.65125 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbad7845-72dc-3a34-91af-745e2d44a017 | -10.23985 | -50.31374 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 4d6c3e91-2a5a-3686-a214-95afa7f3b7ac | -10.83234 | -46.62328 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33b77689-c6c8-37c5-90b2-11efcccc327d | -9.33258 | -45.71597 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b18740f-5504-3667-8f55-3e4468c94821 | -11.87403 | -45.02312 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a128f3a1-e8b3-36a4-827f-b1ff0155bac3 | -7.80344 | -46.02036 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89b33045-2cff-3c71-bbd8-2ff26e46bff7 | -6.8272 | -41.62086 | 2025-10-02 04:29:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 283be780-301a-3f95-acbb-19226ca2a300 | -7.33749 | -45.9541 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afadc3ac-eecf-35ca-943c-36d5caf35043 | -10.85463 | -45.40826 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f08f7d61-637c-3d3d-b35f-c4139f99f0b0 | -10.85356 | -46.66303 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 150c9970-1d61-31f3-8b70-e1496e91b934 | -11.42895 | -47.2871 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b66294be-20bc-3ed7-ad98-137e4cbd85f9 | -8.54161 | -48.24783 | 2025-10-02 04:29:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7846a778-29f9-3dca-ab1c-fa8e7e091eb6 | -5.94215 | -45.88226 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65cf024d-1a4f-32d2-b4ad-e21452c373a0 | -7.72198 | -46.21873 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 655b5412-1ca0-342a-bbac-5dc8e6c05bba | -10.9219 | -46.46616 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e8749d2-5b12-3389-94cf-e3c7d250aa57 | -9.9433 | -43.75073 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3fd79f15-4db2-32e1-b658-ab32e6e3c9ca | -9.94825 | -43.66751 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4628e99-cef0-3ef4-b75a-d37b88df55ee | -11.59952 | -45.05535 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a42b0621-79c2-39bb-a7bf-dd7605f38542 | -11.8541 | -44.9874 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbc5a67d-f539-36fd-aa24-1ea614826650 | -8.81567 | -46.68224 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5aade2c-b9bd-3cd2-962e-ed31219fe1d8 | -11.67837 | -45.32258 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cac4fba-354c-3008-99a5-16da04be4053 | -11.00093 | -46.54419 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d9dcc39-3923-362f-b699-035baaf2eab7 | -5.62117 | -51.93766 | 2025-10-02 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab97f257-e637-3b45-9067-7047c9a7ac88 | -11.81534 | -47.68888 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09d6cb9f-1de2-3a97-9a8f-6e0fd22b7e1d | -7.05279 | -43.27458 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5b3a5777-4543-3eaf-a1a0-a2fdbbf89b52 | -11.85995 | -44.99659 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 70edc66d-54a0-3ec2-93d7-e027f67c28d7 | -11.50001 | -43.50617 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee8fe192-59af-3887-824a-4a4b27f7dbe8 | -11.18498 | -47.82173 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4d0ad77-db56-3a33-a277-94c36828fed3 | -6.70915 | -44.56945 | 2025-10-02 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0798575-ec8d-3551-ac37-d392fc84a5db | -11.19953 | -47.77338 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 539b48c9-8558-39c1-9be6-7192dfee61a5 | -6.82524 | -41.62461 | 2025-10-02 04:29:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6a368f7f-b7eb-30f2-a4aa-ac3320834943 | -5.83844 | -45.74421 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfdf2986-c0ba-3400-8f77-1ad199def3e7 | -7.00814 | -42.31475 | 2025-10-02 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 09d0f7ec-3f78-385c-b7e7-f83cf196e132 | -10.33365 | -45.26095 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0575fbeb-6bd1-3cb2-af35-54c7142c6ddc | -10.34633 | -43.73817 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22ba353a-1ba2-3b87-8d4b-e7546482e062 | -10.83225 | -45.37003 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 005e3280-23bf-371a-8461-d60145444eea | -6.63466 | -43.68338 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18433688-c43b-3aeb-89e1-1519e1ac49a8 | -11.17517 | -47.28573 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| b2b19f58-5a54-3c8c-a2a9-cb02b01eb4e1 | -6.82085 | -47.98024 | 2025-10-02 04:29:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f61af5f-dd4a-3f42-883e-837a9e1859e6 | -10.90887 | -44.78705 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a4f6b50-1ae5-3321-b2f6-b1073229cedf | -6.31535 | -44.11999 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37a976bc-2524-3d67-a0b3-1df36c481283 | -10.68784 | -48.56149 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bee8cc87-c392-380e-8430-a8a753e08f8b | -11.48487 | -43.50392 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be4b3eea-7f5d-3247-a2d2-1910f07c417a | -5.93882 | -45.88174 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fea3d06-9281-3b09-ae0f-b47115218978 | -6.67087 | -42.79338 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1b54b385-43c4-3a6c-bafe-62dd3d3dee99 | -10.84433 | -45.38336 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53942da0-98f4-3ece-bdbb-6dc0c4e15ae0 | -8.82717 | -44.78941 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa09018c-63a7-35a9-90d4-8a678f5e08b2 | -11.811 | -47.58686 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README74.md)
