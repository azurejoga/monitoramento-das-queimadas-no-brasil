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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| beaca12c-494a-340e-a018-312eef4d7db4 | -3.54074 | -50.40124 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68eff006-eb56-326b-9401-69563231ac9f | -2.54442 | -45.39116 | 2024-11-27 04:42:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2e1a9d5-87ab-365f-9a66-21221cff6e95 | -2.83366 | -51.28534 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5eb6e1c-08f3-388a-a48b-d030f1789dd7 | -3.09172 | -50.36199 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d46ee1d-83ce-3263-96e6-b533a8084934 | -3.96508 | -48.07997 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bd789695-2bd9-33dd-bae4-87c57691af46 | -3.55005 | -50.3851 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29c479e7-fe9d-35c3-bee0-329fa828a51e | -0.76279 | -52.46027 | 2024-11-27 04:42:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c377a21-50f0-32eb-a625-d9345bec92cd | -5.25519 | -40.60446 | 2024-11-27 04:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 306e9729-95be-3ce1-88ee-8cf83b94372b | -2.38574 | -53.71166 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0f854a1-f50d-3371-a611-01696ddfb75e | -3.29511 | -50.62328 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1ae6291-d524-3677-84a3-a607ee0dda0e | -1.55256 | -52.02063 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d33ac716-8f4e-3b3a-a1aa-feb2ca419a2d | -3.09278 | -53.24555 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 813cba88-cbb4-306b-a28e-b52a9e20ec59 | -2.82108 | -46.81833 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a53a4fa4-895f-311b-9443-062a0ee51bf2 | -1.24393 | -51.6233 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2583c838-25c8-3606-8b78-2d7bc17b469d | -2.82224 | -48.61045 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6afd4705-8683-30c2-b0ac-fd2df8334376 | -2.82937 | -46.83688 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1ade0e8-1a36-3412-8cb5-261ef6465670 | -3.27788 | -50.56061 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eed03cd-011e-3196-912a-dd2b51ac7d16 | -3.97897 | -48.08218 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c806f62-873b-30e3-9c3e-ace97e46d812 | -3.25504 | -53.7063 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56aa498f-d197-3738-b125-f01069b1c2dd | -0.27259 | -51.62292 | 2024-11-27 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8b77a07-eb0c-3660-9bab-0b30e4c29ca7 | -3.73091 | -49.94789 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f865a71-6923-3253-b8dd-4795729e6126 | -3.18278 | -48.43092 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9915f448-d1d9-3ad3-8f7f-0c036e266cc2 | -2.92716 | -48.6337 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33ad35c7-41a1-3913-9d04-bf694318a2f3 | -2.85984 | -53.32059 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99f151d3-d96f-3a20-ba64-e7a9c248b6a9 | -2.57041 | -49.09558 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9bf69b38-1335-378f-ae95-9080aeec94b3 | -3.27149 | -51.26726 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1292eebe-515f-35a1-af09-3d82851ea384 | -3.10681 | -53.27292 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da623290-4773-328b-a2d0-9ec706ba6d3a | -1.6738 | -48.46507 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9608f8f1-8b3a-3e38-af5a-5bfc6513407a | -1.72046 | -52.15385 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 137b2e8f-ed6e-35cb-ae2c-386f2f3f4261 | -2.5597 | -48.20154 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe7f25a0-76f5-3da9-8fff-4fbdcb00e445 | -1.7934 | -52.7434 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4fabf495-2a98-3742-a29e-791664e2eb1d | -4.27144 | -48.61714 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 568732b6-2bf2-3018-ad81-61a27a474e64 | -2.80124 | -52.91702 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39b34202-7b16-3d9e-8f76-279ad71626e5 | -2.58537 | -53.96701 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 072f949b-4168-3706-9581-cd5e050af16c | -1.31301 | -51.73975 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69c4f4b9-a538-3040-9401-02f8cbb8da1f | -3.11071 | -53.24832 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b0de84a-b157-342a-b54c-882c26377000 | -3.09887 | -50.35958 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b268d8b9-6d93-3dda-8023-f22474a707b1 | -3.28537 | -51.11528 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42582b1f-e9fa-3e43-a3d1-e19dbe47046f | -3.88492 | -43.16124 | 2024-11-27 04:42:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a41e3de-9cea-360c-bace-d9a9b7c1b69d | -1.76369 | -53.62422 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c00a2f31-c11e-3aac-8fd6-a04d108cffe9 | -1.2254 | -51.80581 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92870a7b-7b33-33d8-b247-dda806afb253 | -4.0008 | -47.91574 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73f3929a-4726-3a39-a897-4284733e40f7 | -3.40773 | -53.2004 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 018b5d2b-d333-3093-addb-be4aeb87c15a | -1.95036 | -46.26298 | 2024-11-27 04:42:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06c941bf-b1dc-3922-b8d9-41c4867e736b | -3.04052 | -48.5141 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d22f4a3-b3b4-334d-912d-f3611e1dc055 | -4.25606 | -48.67126 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34a095a3-44a3-3487-b151-ab5f98dbd7ea | -0.94795 | -51.65359 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf5a5b48-6936-30b8-ad0a-a47e0237fbfb | -3.10518 | -53.26001 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 182666cf-3278-37b7-a44a-4b1f7dffeefc | -0.47878 | -48.63578 | 2024-11-27 04:42:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7550d5c-f8f3-3ba5-89aa-569e7abad854 | -3.05325 | -53.28545 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c3bed3e-c312-3480-87a2-116e139be4c6 | -4.13887 | -54.33805 | 2024-11-27 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92b73911-0fa1-3162-8bbb-a3ace3e6ccce | -2.54467 | -46.40614 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eab8c401-e087-3328-9a38-020f15082d98 | -3.08167 | -53.26901 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 060f67a7-6442-3713-8234-ef2b10f8bf33 | -2.69815 | -51.98269 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 123ded9f-73be-382c-8631-ba9af5b5d62e | -1.42382 | -54.8911 | 2024-11-27 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c809b3f-66c8-3053-b62f-24a1922c2c11 | -1.64785 | -47.71073 | 2024-11-27 04:42:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85509c92-0a17-3d36-8658-f7533d235fb0 | -1.66302 | -52.71944 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b845222a-323f-32c3-bc97-67d18103fc54 | -2.57101 | -54.05831 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 684bf568-9ae0-3b9d-b2ca-d616b7e125d3 | -1.15147 | -53.67739 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd9de8fd-6a82-394a-b36d-4e5d67e26b69 | -1.66147 | -46.94217 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcf2609a-8516-39f2-81b8-dfed01d245af | -3.59408 | -50.38492 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30faf195-059e-3a59-aa7c-993bbc740bac | -4.21278 | -50.90197 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27f8023c-6217-3264-96a7-70d53fcf287a | -4.29022 | -48.1985 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23c1b1c5-186a-3f28-b988-549492c7d3dc | -1.76652 | -52.70638 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1335ed0-5a32-3a0a-876d-33540ee6d94f | -4.23052 | -48.70113 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 820d7c59-244e-30a0-b2b7-b7ac13a29883 | -2.79172 | -53.02192 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a60f6a82-8e25-3802-a748-6d5335d40d19 | -1.62784 | -52.27755 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75b7d0a9-215a-3f3b-b3a6-5ea3b33abc84 | -2.7001 | -45.66236 | 2024-11-27 04:42:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5a480d0-3c09-3a78-a82d-a0bad94f95ab | -3.70977 | -47.6654 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ba83856-88a6-3d79-b3fe-27ed8d7697f6 | -2.80338 | -53.04029 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8421feb0-1df9-3c5e-a690-9cfb1c390cb7 | -3.2877 | -50.51984 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c21fec73-7c30-37f2-a344-f75adcc2c716 | -2.80752 | -54.13203 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d8bef5c3-78f3-39f5-9200-2b7551f17b67 | -3.10995 | -51.25966 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c367394-052f-3d10-8bd5-f9df20cd0655 | -4.2481 | -48.67758 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 25cd7321-0a18-321d-adcb-e6970c1bcd59 | -4.00378 | -49.96247 | 2024-11-27 04:42:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8ccc56c-f39c-3e95-937b-383d6fea186d | -3.08431 | -53.25253 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fe61639-4aa6-32df-b227-fdeb83c240c4 | -4.03842 | -50.30312 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 045141b7-9998-3b78-afef-06fd55fbe7c6 | 0.94782 | -50.73177 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3125bd0-675d-3a20-a57a-29404adc738c | -4.24981 | -48.66655 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47d6f519-6903-3e7f-a17b-adc247001144 | -2.45706 | -53.70763 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13ab36ac-885e-38c6-babb-6473db3ca627 | -3.97503 | -46.72853 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73c1547d-06ba-32d5-a3ab-235881d7dd98 | -3.34623 | -50.19096 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 035a8f23-532f-3aa3-911a-faa986b15b9e | -3.77088 | -52.40219 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f56e5414-6ce7-3d17-9f77-228fa8cbed07 | -3.88565 | -43.15636 | 2024-11-27 04:42:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bcc13fed-e77e-35c3-a010-bc70a35bf754 | -3.05361 | -53.67854 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33735161-d3a6-3101-9124-a075ee947037 | -3.49741 | -50.46139 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09419dbc-1d9a-3d84-a857-432faf44427f | -1.95721 | -50.57563 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4710b794-33f7-3cbf-957c-7c97825af635 | -2.73298 | -54.11256 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4efdc19c-f482-37cd-830f-05f70c7a3307 | -3.10336 | -54.98019 | 2024-11-27 04:42:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d31a0901-4b8c-328f-8819-e72eef7d9c78 | -2.94974 | -51.43325 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd3687f6-bd09-338f-8d98-1961fb9f2bab | -4.24089 | -46.2442 | 2024-11-27 04:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1f0defd-05dc-3906-bd6c-55257aa11844 | -2.58214 | -50.64191 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a76b1341-b0c4-3a41-bbe1-3824ec2bf3cc | -4.72974 | -46.57154 | 2024-11-27 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac114f4c-1d9d-3199-a3a0-e4cae8d2e59b | -3.3901 | -50.32098 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2975ed00-89dc-340a-91e8-64b003bfc6d3 | -1.76304 | -52.28954 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5501601e-2ff6-3534-9b3f-170ae5af2bfc | -3.50073 | -53.80736 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| edb90e5d-51c9-35ec-bb5d-79e2e744a4d0 | -2.99536 | -47.34696 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e251a843-ef83-30e8-b4bc-24cf4c05d5ee | -4.08647 | -49.73763 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c619daeb-05e4-3554-8ffc-4c0d9d656fcc | 0.20305 | -49.86019 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56f8847f-342e-3540-a036-3873ccc0e2ea | -3.71283 | -51.80111 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README63.md)
