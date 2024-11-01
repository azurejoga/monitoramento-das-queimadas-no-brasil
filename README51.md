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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e46df221-11cc-3ff4-ab05-9e2f6332648a | -3.0539 | -49.4683 | 2024-11-01 05:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8f9d15e0-db8f-39b3-bfc1-ba192f42fac1 | -3.4134 | -43.9876 | 2024-11-01 05:35:25 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4e45cad6-ba38-3225-8eab-259862425b37 | -3.4321 | -43.9868 | 2024-11-01 05:35:25 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| a699dc94-2c7e-3661-9ab7-3151ada0cf86 | 3.4267 | -51.25449 | 2024-11-01 05:44:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e9e9d72-5db0-3f11-b389-41850bbabd09 | 3.42555 | -51.24796 | 2024-11-01 05:44:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 187eb3c3-160f-3b61-878e-f7704c4d367e | 3.42089 | -51.26221 | 2024-11-01 05:44:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d892d15c-bc59-3e49-bc5d-a4fbe98e7d8a | 4.05938 | -59.88271 | 2024-11-01 05:44:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c80e077d-2539-3d64-ba35-d3b67776f147 | -3.0539 | -49.4683 | 2024-11-01 05:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6e9ac88f-ddb8-3b54-bd51-9ab8ac2500b3 | -3.0538 | -49.4895 | 2024-11-01 05:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| bf0ece53-0768-37e7-afb7-98de640be3bd | -3.0354 | -49.4688 | 2024-11-01 05:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 532faf79-b971-3a34-8291-e05a4f9c3dff | -3.0353 | -49.4901 | 2024-11-01 05:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 34973965-9217-34bb-988f-ad554f7db5eb | -4.4054 | -43.4746 | 2024-11-01 05:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 5915c6d8-7df8-32f7-aa15-459db32e43bb | -2.73635 | -66.0213 | 2024-11-01 05:46:00 | NPP-375D | JURUÁ | AMAZONAS | Brasil | 1302207 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd3bd6bd-ef44-38ed-bc6e-0b61e5febdea | -0.68954 | -51.67655 | 2024-11-01 05:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14e4e03d-7ddc-3d31-a93d-f5f981c5c146 | -0.68517 | -51.67434 | 2024-11-01 05:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bf7ba66-070e-3123-b463-3350d8b3020e | -0.68408 | -51.68141 | 2024-11-01 05:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a2db9b8-5cb8-380e-bcf5-729c7c8750a9 | -0.68235 | -51.67543 | 2024-11-01 05:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b4acd80-2edb-37b1-9f27-9720d6f34b30 | -1.60393 | -52.37571 | 2024-11-01 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70d56570-9d1f-3125-90b2-e18ec66ea5a8 | -1.6029 | -52.38227 | 2024-11-01 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9d1f88c-9a00-32d4-b3a2-bc9a03ad147b | -1.60263 | -52.37465 | 2024-11-01 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7badb21e-2501-32d2-bc23-70464ef959ed | -1.60165 | -52.38121 | 2024-11-01 05:46:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7550f42e-3bfc-3740-bf2e-ab17cef4e4ed | -1.43255 | -52.20024 | 2024-11-01 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db755d80-fadf-3aa3-a918-8711f3a436d5 | -1.43154 | -52.20694 | 2024-11-01 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cfaf8f0a-ae90-37f6-bf31-324898b03ad4 | -1.42764 | -52.20057 | 2024-11-01 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 222e83cd-0889-3183-977e-8e7141a18cb9 | -1.42551 | -52.1991 | 2024-11-01 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86b20476-945c-3ee5-8d07-f8baf506a2fa | -1.42059 | -52.1995 | 2024-11-01 05:46:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ec3adf37-d015-3bfc-9203-952d50b2af4f | -3.25629 | -53.07079 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64e46e1d-5e32-3d76-ac45-edb8840e3842 | -3.24945 | -53.0696 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8fdd83b-8846-3ec4-a003-76b4708ba98d | -3.24005 | -53.36842 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e1c8b5a5-e185-3088-93d2-d6c810ca3c8e | -3.23501 | -53.36735 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 14e43450-d9e8-3f79-bb50-9f54d2f31f06 | -3.23327 | -53.36766 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 72c1a267-6bb6-37f0-8473-3a18793cc028 | -2.88205 | -52.8925 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1491155-4e89-3429-add1-a944f70e0c1b | -2.88129 | -52.89116 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11c51b30-a982-3c85-b1bb-80f7ef2c0c9b | -2.88033 | -52.89788 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4559905-c0c6-3fcb-88b5-6d20f85ebb1d | -2.87517 | -52.89129 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 50e3a1f7-1bbc-3776-a745-611004c1a43a | -2.8744 | -52.89002 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ad05c82-a30e-3461-874a-e8cc86574863 | -2.8742 | -52.89779 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 42fcca00-2aa6-3ff0-a798-86dde51b65e9 | -2.87348 | -52.89651 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62a58077-9b13-3a94-9819-b7b61df2aba0 | -2.86826 | -52.8903 | 2024-11-01 05:46:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fce91219-6773-3872-9e24-6da8bd3ff722 | -1.46805 | -54.23361 | 2024-11-01 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| efcad556-ba73-36b4-a1eb-b3d4b99c4b57 | -2.16297 | -53.67443 | 2024-11-01 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4f711b53-2b68-3251-807b-702a29e5a9ff | -2.16214 | -53.67977 | 2024-11-01 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 551ca39d-1dfa-336f-b748-580d63a99a52 | -2.16156 | -53.67447 | 2024-11-01 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b75c0873-be2f-3a6a-a573-db322dd26710 | -2.16077 | -53.67979 | 2024-11-01 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3e205dae-3640-35df-bc52-306837d280ff | -1.17422 | -53.68274 | 2024-11-01 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed4fee75-5c0a-3176-aef8-e7ebf5865276 | -1.16774 | -53.68205 | 2024-11-01 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d5df965-01b0-368b-bf6f-26d5aca91cfb | -3.12171 | -54.29993 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99ec6873-579a-3a4a-9f0d-99b32bfaa9ca | -3.12132 | -54.25744 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81fc9fa9-27b2-3cf1-9dbf-023c89eebb31 | -3.12055 | -54.26275 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 587e2ae2-a2a4-328d-a1ad-cc68b7d0c815 | -3.12041 | -54.29907 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c1610ac-0899-312d-b27e-bd4fbd930b16 | -3.11979 | -54.26804 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1f82152-7032-3266-af91-29eca601d7c8 | -3.11949 | -54.26202 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00b2193f-93e1-3311-aff2-a2d47904bbb9 | -3.11904 | -54.27326 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f36059cf-4bee-396c-acda-8c6daad01d78 | -3.11869 | -54.26728 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f2fc10a-48e0-35ba-a730-ffb19d206e8e | -3.11791 | -54.27251 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c279c8c-06b7-35d6-879c-72e203227376 | -3.11608 | -54.29387 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 812b7c55-7264-33fc-9247-e393023c7d65 | -3.11535 | -54.29894 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 100d0a11-ad00-3147-b128-5b227d1e1da5 | -3.11417 | -54.26185 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88ffae43-7614-3ee7-ac86-efdc0e6b045f | -3.11404 | -54.2981 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbf27945-6bca-3c97-aeb1-02131218dcab | -3.11341 | -54.26711 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b49c7abf-73be-3e6d-adbe-645fdb6cce94 | -3.11231 | -54.26638 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a26f0aae-4d94-3bb0-87b1-37a40ff9a3d5 | -3.10483 | -54.28161 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04a369c8-b354-3261-806e-4d8bdffd695f | -3.10362 | -54.28086 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ed020b0-ce69-34f4-936e-0d2ac91b0f87 | -3.09847 | -54.28058 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cd3ec05-d598-398b-92b8-aebe7eb2c88e | -3.09726 | -54.27983 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d628ba5-3611-386e-90c7-ef68985bd42f | -3.06867 | -54.16412 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0535a0be-1489-3aec-a254-a78c3f959241 | -3.06788 | -54.16949 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5141aab2-4dc6-32ff-b925-6714e9fc6aab | -3.04867 | -54.16649 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1e1c62c-42ab-3e65-a679-70d18d0fac0c | -3.04792 | -54.17165 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2ec4dae7-32da-375c-8290-4ebf9962bea5 | -3.04725 | -54.16539 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0423ff5-4e54-3a48-9f1e-18ace89060d3 | -3.04647 | -54.17054 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adddddbf-6a7b-351b-9dd7-55593bcef327 | -3.04568 | -54.17575 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 33f6524d-093a-37f7-956c-6861650c3059 | -2.97949 | -54.6417 | 2024-11-01 05:46:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf36f6c1-d359-3fc9-be3f-14d8993fd7a5 | -2.91881 | -54.19347 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef93a3f4-92e0-3e05-81bd-f962315dd7be | -2.91806 | -54.19865 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26cc002d-eb8b-3205-a21f-c6d07213e6fd | -2.91786 | -54.19309 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26f070bd-32aa-3637-aa27-dcbafc483cfa | -2.91708 | -54.19827 | 2024-11-01 05:46:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8facb0b-cb6c-3aff-a567-e4fc90b6a678 | -3.48475 | -54.02994 | 2024-11-01 05:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae11e995-82c0-3c50-8a0f-b26d352bc398 | -2.4737 | -53.98024 | 2024-11-01 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8624e0a2-9d78-3972-a67b-4f8e93a5ff55 | -2.47295 | -53.98526 | 2024-11-01 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daef0fcb-3e30-3ea4-9784-af80d4b58626 | -2.46651 | -53.98439 | 2024-11-01 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76960638-0121-3a66-aba7-668da3664731 | -2.10948 | -55.92059 | 2024-11-01 05:46:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 699bb141-853c-3ece-ae8e-fb40c41bf45f | -2.10333 | -55.03152 | 2024-11-01 05:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d59c3c5-61cf-3309-b352-057992b95d5a | -1.81492 | -57.10361 | 2024-11-01 05:46:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91f9eeaa-2d40-38f2-b36a-bd80510c340b | -1.81443 | -57.10681 | 2024-11-01 05:46:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ea1c921-2ac7-38bf-82b7-3ead6fbc009e | -1.05849 | -57.40364 | 2024-11-01 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aee42750-432a-3109-9684-ce1108beb897 | -1.05804 | -57.40658 | 2024-11-01 05:46:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 000cff8a-787a-3c34-a21f-3fbf6b378f27 | -3.28581 | -61.22537 | 2024-11-01 05:46:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11710a7d-acdc-36c3-aafa-361507a1a918 | 2.57659 | -60.69777 | 2024-11-01 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c802085-1252-3f71-b9dd-647ce1f7f55e | 2.57278 | -60.69838 | 2024-11-01 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24516b8d-9700-311f-9eac-241d2dfbd3d1 | 2.57204 | -60.69372 | 2024-11-01 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 96b4a4e6-4591-3f33-854d-12bae071f066 | 2.56897 | -60.69899 | 2024-11-01 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eddc8989-a065-3786-88c1-7058ad550e93 | 2.56823 | -60.69432 | 2024-11-01 05:46:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6cd588bc-2ee8-3548-877d-64d4807c72ef | -0.7577 | -62.9007 | 2024-11-01 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5a88430-7987-39d2-9182-807ddc0aef5c | -0.75479 | -62.89621 | 2024-11-01 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5a8494e-96f1-38aa-9add-6ceeb2405931 | -0.75417 | -62.90014 | 2024-11-01 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cf37418-8610-39dd-a3ea-6a8cccf3b779 | -1.07125 | -62.65197 | 2024-11-01 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e4bd430-e2d8-308b-afa1-0a5192bb7b5f | -0.79759 | -63.08271 | 2024-11-01 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51f4b6ac-6d45-3819-b987-990ef89aa513 | -0.7947 | -63.0783 | 2024-11-01 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0534f8c5-d33c-3d92-bd6f-14d00a78c492 | -0.79408 | -63.08216 | 2024-11-01 05:46:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README52.md)
