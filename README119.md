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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8ad5e94-06bc-3acf-ae37-fa467c250e21 | -14.1819 | -51.7866 | 2026-09-21 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| b8f7d699-638a-31fc-a9bd-40cbdbfff208 | -6.2026 | -57.7778 | 2026-09-21 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 27dececa-cd49-36da-9001-0118522f4581 | -8.7914 | -48.7285 | 2026-09-21 13:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 9e8df32d-6cd4-3b48-90b8-d4a515a86ebc | -11.118 | -54.0268 | 2026-09-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 420ad5d1-656e-3854-9ee8-62fb7a309414 | -12.4016 | -47.003 | 2026-09-21 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 369b93b2-04e2-3f9c-8617-e91b11ad7574 | -11.041 | -54.1567 | 2026-09-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| e1921883-9e5d-3bc8-b2a3-f7bd17cc9787 | -8.7911 | -48.7502 | 2026-09-21 13:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 5694d34c-62b9-3d54-b279-e80ed7ac1097 | -11.9507 | -46.5033 | 2026-09-21 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| cac54e2e-3adb-351c-bf32-e5eb72276c08 | -11.7823 | -49.8152 | 2026-09-21 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| bec932d0-2b18-3bc8-8b66-1b86031ceb4f | -6.9034 | -42.9341 | 2026-09-21 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.8 |
| cc8738a3-5e01-38d6-a46b-0a88877ecf20 | -3.5654 | -43.4727 | 2026-09-21 13:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 252.4 |
| 65703e22-6120-3b14-8650-9de195cecddf | -6.728 | -59.423 | 2026-09-21 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a109b47a-357e-3faa-8cc7-cf3b4465fc1e | -10.3728 | -48.8936 | 2026-09-21 13:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 34e76119-912f-3c01-b4ad-f79b3e86e665 | -9.4567 | -45.4178 | 2026-09-21 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 2a3245cb-59fc-33b7-8500-f284cf00aebb | -3.1881 | -58.5855 | 2026-09-21 13:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| aa70be2a-a18c-3b89-8bf1-a7d135368862 | -13.2596 | -51.7973 | 2026-09-21 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 648a5eed-ea4b-3bf9-a41d-d12a7706f91f | -10.8093 | -50.1621 | 2026-09-21 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 1dfcb376-3124-3855-af8e-9a87840c999f | -11.0412 | -54.1362 | 2026-09-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1f7d3bf2-795a-3075-ae8f-c03d8c85e393 | -6.9225 | -42.9088 | 2026-09-21 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 6920591e-f6f0-31ab-b7d7-747c6110f89b | -4.6835 | -46.4074 | 2026-09-21 13:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 50244b10-84a3-388c-9ac3-dddca5419f31 | -12.2723 | -50.1657 | 2026-09-21 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 13021a4b-be1b-3803-8a91-7d7468d1e9ad | -11.9969 | -58.0622 | 2026-09-21 13:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 74145c55-1045-3224-800c-582a90e9b65f | -11.8715 | -48.9792 | 2026-09-21 13:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 54319d4f-b289-3acf-b36d-6f75bd8c8d6e | -8.7911 | -48.7502 | 2026-09-21 13:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 848b29c8-51a4-3a2c-be4d-088f7993dfa1 | -6.9225 | -42.9088 | 2026-09-21 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 97e3b891-1b3b-3733-b8ea-d62945e65c7c | -7.4283 | -44.7639 | 2026-09-21 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| c14719ef-6c23-3dc3-b6a5-ff089afc5d27 | -12.8056 | -54.0462 | 2026-09-21 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 55938f5f-ac9f-358b-be14-6dbff47c78a6 | -10.3549 | -50.2099 | 2026-09-21 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1005210a-cb54-3719-bcb6-d777848f3593 | -6.7464 | -59.4223 | 2026-09-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 179.7 |
| 60115455-1f30-3eaf-8f34-a5b6c07cf0ee | -10.3917 | -48.8915 | 2026-09-21 13:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 24449056-ae5a-3fb8-b14d-73c3db4efb1e | -14.0421 | -52.0812 | 2026-09-21 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ba17c886-8977-3c78-abbf-39148260c865 | -10.8662 | -50.156 | 2026-09-21 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 61b885ec-d3e7-386e-9f9a-22bf484787cd | -10.8093 | -50.1621 | 2026-09-21 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| ce81a765-868c-3479-8a72-c80b2509a424 | -6.2026 | -57.7778 | 2026-09-21 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| cab76f93-76d3-323b-ba4f-6758c38e2c18 | -10.8735 | -53.9668 | 2026-09-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0f56e4af-d24c-3bfb-8110-8b847ed45bac | -6.4485 | -59.9909 | 2026-09-21 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 7ea5e2a5-589c-32c8-ac59-f530cbfa6767 | -11.9967 | -58.0821 | 2026-09-21 13:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 00be14d5-025f-36b4-98de-8e168c9cfd08 | -6.5759 | -45.5419 | 2026-09-21 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| c1b7e4db-d029-367c-bc51-7b4dfa72a3fd | -8.7912 | -44.301 | 2026-09-21 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a5b6bb0b-7ef8-3d85-b77e-3c49fa14ae13 | -9.2756 | -46.2077 | 2026-09-21 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c016c2f0-a798-390c-a6c2-862c1869161d | -10.4675 | -50.2624 | 2026-09-21 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| fdebb863-c2cb-35ae-8120-3eb832287d94 | -12.8246 | -54.0442 | 2026-09-21 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 6d552f9d-7c5c-398d-a554-c49c17069db2 | -9.4567 | -45.4178 | 2026-09-21 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 1027fde1-4963-335b-a8b7-868cfc22fdea | -6.728 | -59.423 | 2026-09-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 5a9fc198-29be-3543-89d5-5cb648bec1b6 | -8.1876 | -54.7219 | 2026-09-21 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 60665aa6-b67d-391f-98ca-ade85ed1d048 | -7.5889 | -57.6757 | 2026-09-21 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ad9774c8-a450-375e-8c15-0d27c30894c1 | -11.8682 | -46.8529 | 2026-09-21 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| aefc229f-d762-3b9d-ab69-38ee29fb55d1 | -14.0425 | -52.06 | 2026-09-21 13:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ddca5107-c765-34ad-9f5c-eae9112157b7 | -10.3725 | -48.9153 | 2026-09-21 13:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6e9f577b-7043-3bc7-9267-ae2c4362cd77 | -9.238 | -46.1894 | 2026-09-21 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| f7aa7b86-1469-3144-ac1f-315423c64291 | -11.3419 | -51.3606 | 2026-09-21 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 68fe95ea-c12e-3b5d-afa3-078a67c38970 | -11.8715 | -48.9792 | 2026-09-21 13:30:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 173.5 |
| ab70a2ec-7133-30ba-a5b7-58174b810733 | -11.041 | -54.1567 | 2026-09-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| aaaabe75-d95c-31b7-b48e-bfc3d6702193 | -11.36 | -51.4221 | 2026-09-21 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| f00c04f8-5280-3652-9d4d-3c0ed574cda6 | -6.4671 | -59.9711 | 2026-09-21 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 93f9d527-6b01-3fe1-8780-e77a1522d56a | -7.3289 | -55.2155 | 2026-09-21 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 90d78e9c-a18a-3935-9cbd-5a5f4d36470d | -3.753 | -59.419 | 2026-09-21 13:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 76f33384-74a9-34e9-acb2-2d1be2d84836 | -10.279 | -50.2391 | 2026-09-21 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| e95d617d-6d0d-3153-9b2c-2d067367f27c | -11.0412 | -54.1362 | 2026-09-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| bd5741ac-67ca-3f90-a5d0-740638cadf69 | -4.0142 | -53.4946 | 2026-09-21 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 46e9596d-c195-3f39-bdc8-bac44dc5e95e | -10.3914 | -48.9133 | 2026-09-21 13:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 2cdc15b7-2500-3f0b-91f1-b927e5bf196a | -5.9335 | -59.9515 | 2026-09-21 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 161.8 |
| b0b00b18-70a8-3d7f-9afc-81efab350153 | -8.7914 | -48.7285 | 2026-09-21 13:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 66ddd9bc-dbfe-3566-9d19-d48696f2c453 | -7.4092 | -44.7885 | 2026-09-21 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 4dc4c96f-b689-3c83-8946-cd5672c18610 | -10.7999 | -50.8455 | 2026-09-21 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 58c49f8b-ffb1-3e93-82b1-f1cf65d95e81 | -8.7729 | -44.2568 | 2026-09-21 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 8760169d-4914-3431-978c-5ef974b83751 | -10.8282 | -50.1601 | 2026-09-21 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| b1143144-0683-39dd-9956-efb480776334 | -7.3291 | -55.1955 | 2026-09-21 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c094e944-89cb-346c-b3eb-25ad34999dce | -9.977 | -50.248 | 2026-09-21 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 33fe1e31-6a8b-3606-9b56-582787b23e5c | -4.2239 | -48.6127 | 2026-09-21 13:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 49f839ba-6773-3210-b5eb-eb641a87e604 | -10.8011 | -50.7604 | 2026-09-21 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 6c1ae5c1-d888-33e2-9e37-2bee555e339a | -8.1874 | -54.742 | 2026-09-21 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 09274819-1cf9-3954-b9df-757cbe45893e | -4.9533 | -45.16 | 2026-09-21 13:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| fef184e1-4a05-3f6e-a266-8039c8e4025e | -11.6802 | -43.4209 | 2026-09-21 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3e8b6f96-bb9d-3694-8935-58b6be5cd639 | -11.8014 | -49.8129 | 2026-09-21 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 28542d2a-934b-37ca-9e26-37c0f62557ec | -7.0575 | -49.9001 | 2026-09-21 13:30:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| dcbda413-b62e-3f54-a332-4c29f07d2c7c | -10.3728 | -48.8936 | 2026-09-21 13:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 3ec89d40-504c-3db1-892a-cf563e689ae8 | -10.9112 | -53.9635 | 2026-09-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| bd06f375-bb72-3ffe-961a-b82a91ab4429 | -10.9361 | -50.5759 | 2026-09-21 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 760986be-096e-363e-9ff0-d59b0854f6c3 | -10.8096 | -50.1407 | 2026-09-21 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 13d3f6ef-ba9c-3f08-8c0b-532dac8ffc06 | -11.1183 | -54.0062 | 2026-09-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5b8c60ef-de91-3a11-b53f-346e5e41901a | -6.1841 | -57.7786 | 2026-09-21 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 34fcc448-10f5-34cc-bea5-cd51cc03805b | -7.428 | -44.7867 | 2026-09-21 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 92ba818a-4094-310d-93e3-237a68cd0db9 | -8.1872 | -54.7622 | 2026-09-21 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 8ac8af56-dfa7-3814-aa24-a550b90ca171 | -10.4486 | -50.2644 | 2026-09-21 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 36f13d10-a6e7-3602-b8a6-38b065422ca8 | -8.7723 | -44.3031 | 2026-09-21 13:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 1573ba07-9895-33b4-8876-bdb38d770819 | -12.4012 | -47.0255 | 2026-09-21 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 12e8341f-407a-3082-9b9d-e1abea4b9afb | -5.9151 | -59.9522 | 2026-09-21 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 8f5ca7d5-f03d-35ec-9aef-7a5fc3f8b9b3 | -12.4204 | -47.0228 | 2026-09-21 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 276.3 |
| a4e5f837-882f-3d7b-8529-984fcbbade5c | -10.4672 | -50.2838 | 2026-09-21 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 24eafb82-b1f8-3586-9049-da0881ffb1ee | -11.7823 | -49.8152 | 2026-09-21 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| bdb10c43-e804-3c8f-9126-289d06af2f4a | -6.5571 | -45.5434 | 2026-09-21 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| f96211fc-702e-3f08-8999-ce4063fec440 | -12.8434 | -54.0629 | 2026-09-21 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| cffae9b4-3add-39e0-bab3-da732fea8107 | -6.0033 | -44.7247 | 2026-09-21 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| ea5ca262-083e-3810-9510-3426545de55b | -6.5569 | -45.566 | 2026-09-21 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ae14e567-8a9b-35c8-aa40-6e592e9afbea | -5.7615 | -57.5807 | 2026-09-21 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 62fb513f-fd4e-3108-ad1d-5f4b08e76821 | -13.3251 | -51.2997 | 2026-09-21 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 312f1494-edba-3188-848b-76e71e0ad2c7 | -3.5653 | -43.4959 | 2026-09-21 13:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 7beaf533-b646-3556-ae4a-45f2583a734c | -13.2596 | -51.7973 | 2026-09-21 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 225c9dae-0315-36b0-8df4-3c77fb7d1869 | -4.0944 | -52.1252 | 2026-09-21 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |


[Clique aqui para ver as próximas entradas](README120.md)
