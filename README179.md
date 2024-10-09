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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ee379e9-fd6e-3345-9123-cc4d3e569535 | -9.02041 | -60.42408 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee3f8adf-9494-375c-9fc1-9d22aca16b55 | -9.00905 | -60.42218 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 983d9028-0f26-3667-9646-3515252c6af6 | -9.00901 | -60.42422 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 703fa29e-dc31-3742-8e1d-c3eff3118f35 | -9.0069 | -60.73564 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d97358f6-f5fa-31bd-bc3d-58d14e916dfc | -9.00521 | -60.42362 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f92fd1d8-4939-31d6-a2ff-4b21337e666c | -10.39536 | -61.26038 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f278545c-f21d-3ebf-81a3-bb337672a004 | -10.39268 | -61.22969 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b15e124d-1839-3ff5-bfa2-fa53d03d110d | -10.39237 | -61.25262 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31a67681-7fb2-387b-ad06-57e654e5aa81 | -10.39228 | -61.25498 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4f537cb3-b962-3ea4-8ee2-691c3b43864d | -10.39182 | -61.2346 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b0e94f2c-8349-3e80-8cae-3cf64e12d059 | -10.39179 | -61.23213 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dad23231-b620-382d-b1a2-c04ed3f4f598 | -10.39157 | -61.25736 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d9fccfc-c0bb-3c4c-b375-c373a42f1e9f | -10.39147 | -61.25963 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e71555c-2444-317a-bcd9-47bcd1b4558c | -10.39096 | -61.23952 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dbf0d14c-6e42-32dd-8c50-91af1d478920 | -10.39096 | -61.23705 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6f764084-a63c-37cd-8f26-104bb980b695 | -10.39079 | -61.26197 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2f7e97c-15f0-3fdb-b114-5a0bb1f2dca9 | -10.39066 | -61.26429 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 722ca686-f0db-3d66-8f75-63cb6249c34c | -10.39013 | -61.242 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f42cee65-097a-356e-b318-420cb237456e | -10.3901 | -61.24447 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 48924485-ed5c-32fb-8673-fcb94df151f0 | -10.38999 | -61.26672 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aff8892d-7ad5-3564-a59e-a065596896b2 | -10.38965 | -61.22408 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 507338f1-eaf9-30c4-937d-c082cff9b89a | -10.3893 | -61.24696 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4f41ccd1-7778-3730-becc-b1cc696042a4 | -10.38924 | -61.24943 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 001de7b7-c0c4-3c1b-bdb0-d38e7c678373 | -10.38879 | -61.22899 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94246cf0-cfb3-3a40-80e2-599bb1a3cc5f | -10.38872 | -61.22651 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b671818-89c1-3cb0-9c14-03a34f615033 | -10.38847 | -61.25192 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e88f2231-6a84-30fa-9eba-0df356db03cc | -10.38838 | -61.25434 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 18f40b96-4614-3f64-8236-bdf339028b6a | -10.38793 | -61.23389 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 11aef0bc-91d4-37c4-91d9-bdf7ca354129 | -10.38789 | -61.23143 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c7633b8e-c8f9-3c2a-9802-1adcaa834d49 | -10.38767 | -61.25668 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 038426da-3a9d-3023-bd22-58c7705e783b | -10.38758 | -61.25893 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c8f2429b-135b-3d5e-9e27-36a7d8913504 | -10.38708 | -61.23879 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bbb226af-efc6-3ff2-b5e6-98309d1fa7cc | -10.38707 | -61.23633 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9751ab2-ce5d-33dc-8362-2acab8d13c10 | -10.38689 | -61.26127 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bc7cda88-736f-33c0-86cb-c549764ed207 | -10.38677 | -61.26355 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29cb125f-59aa-3477-a0a1-b01f4239093d | -10.38624 | -61.24125 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9d50bf1a-a1fe-37a2-bb58-7d3c7c2cb3c8 | -10.38622 | -61.24371 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c9df3952-6ca6-33f7-b208-cd32cd3186dc | -10.38608 | -61.26607 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1416c33d-5cdd-3d4d-8cb1-6972efa32a3c | -10.38542 | -61.24616 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e5ef8f39-48a6-3ffa-a91f-f6afd3c8329f | -10.38535 | -61.24863 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 327404c2-e493-3e8d-a2b5-a8e333cc4256 | -10.38489 | -61.22832 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f410dbae-6194-3c85-9ce5-d70a99b1c580 | -10.38482 | -61.22582 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aea2527c-ea65-3027-8cac-977ae2346caa | -10.38458 | -61.25115 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4205c6b6-48fc-3e14-8249-7df5299422a5 | -10.38449 | -61.25361 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 57307ac3-59da-35f2-91c8-d01434bd2fd1 | -10.38404 | -61.2332 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 682153ce-b9fd-3c98-a788-f3296fe3e86b | -10.384 | -61.23075 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e3456488-d888-3624-bcb3-1b2cddf5cb48 | -10.38376 | -61.25605 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04d7783b-74fa-3ed2-ab70-73faedd5de43 | -10.38365 | -61.25838 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1d227aa-d9c7-305d-bb0f-f03049d057d4 | -10.38319 | -61.23806 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d88a8f26-07a7-360f-9b9a-38e5b1b0721a | -10.38317 | -61.23562 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ca8f3e3f-3697-3513-8480-8a24fc836466 | -10.38295 | -61.26083 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff6a6e43-c18e-3864-9870-b8da36b6a9e8 | -10.38281 | -61.26318 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0df059fb-2f5a-313d-ab71-cad271e9d8b3 | -10.38236 | -61.24047 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 892b8188-9bbf-3499-a089-67c3ccb708a5 | -10.38234 | -61.24289 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b88af03-b82a-3283-b496-fbb560157224 | -10.38155 | -61.24527 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bc1e0fd8-7f7b-311b-9561-9e6f5f4b95a3 | -10.38149 | -61.24777 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02b58d5b-be69-3e53-97cd-cf4f9331e508 | -10.381 | -61.22765 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db4f3225-1a69-3479-8445-f82dc52d7cea | -10.3807 | -61.25029 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6802788-ec58-3a48-be5e-f750ffff983c | -10.3806 | -61.25283 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a337c36f-f9fc-3d1e-813f-b3832d5a6b32 | -10.37985 | -61.25537 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eed83293-7ffb-3be6-ac3e-b12c00e20783 | -10.37973 | -61.25781 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b1221ca-9905-3c72-9fdb-2f6993918556 | -10.37929 | -61.23737 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7c0aefc-e704-3dcf-9a25-cfa36138c87c | -10.37846 | -61.23976 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca2775e9-dc1a-340f-9d52-9d725692d258 | -10.37374 | -61.17283 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abb1484b-8a42-34f6-82bf-dbeddb606f12 | -10.17518 | -60.89761 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47ca30b2-1641-3a9c-ba11-8d524b23a9cf | -10.17435 | -60.90251 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98d5b459-4f59-381f-aa78-abb69a33f091 | -10.06903 | -61.11811 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad83579e-f5eb-3ac5-b856-5e0a9bc1ff55 | -10.0682 | -61.12307 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a02f560-1a14-310f-bae1-59f75b0755fd | -10.06596 | -61.11261 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 247b2296-0618-3a85-a0fb-6b5fbde3f30c | -10.06516 | -61.11738 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 110cbbae-04c6-37fd-b71e-277a2b7c4682 | -10.06434 | -61.12222 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60388835-0277-3360-b4a5-90e4b2a136e1 | -9.38981 | -60.90072 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0152b8fb-a28f-3609-bb9f-e233ce0574bc | -9.34602 | -61.01558 | 2024-10-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64d0d557-c91f-3294-ba62-c21b391c2d70 | -9.44761 | -60.39938 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 802d4b05-0322-3e5d-8a3d-bb650b5781a7 | -10.43124 | -60.99623 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70f349f2-f9e5-3113-9251-6f161622f724 | -10.43042 | -61.00113 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccf38570-b502-3b9d-bb49-421d1227d896 | -10.42983 | -60.99364 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 32aa0569-2ca4-3d77-8e0b-4b0b69121e1f | -10.429 | -60.99845 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 14c9b143-9c5a-3e91-adef-c003f1d0ac13 | -10.42819 | -60.99081 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57a0b255-3d2c-36e7-8705-9b74fc42703d | -10.4274 | -60.99552 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1283283d-1571-3605-85ed-4a4e6b83d661 | -10.42658 | -61.00043 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0b521896-5d4d-35cc-86f6-eaf8e69e7a50 | -10.42598 | -60.99306 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| df54a150-d0eb-3ac3-8555-c55af7aa52c4 | -10.42514 | -60.99786 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ae962a5a-faec-3dc8-a139-9373ca7d6e17 | -10.42433 | -60.99026 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3676b666-c319-30d1-8061-d70cd4a7c742 | -10.42354 | -60.99501 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 90c31d28-fc3b-3e8b-bfd8-f323b80f0756 | -10.42294 | -60.9878 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31508cb3-9a40-3072-a74a-ff719fc2c8a8 | -10.42272 | -60.99989 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 34e7906b-e5e2-3c6b-ad56-2ea1273f5e74 | -10.42211 | -60.99255 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 88f19aeb-fa55-3f69-b060-e783b611a533 | -10.42128 | -60.99734 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bc52f108-782d-3077-b38e-86fb5d3fab90 | -10.42048 | -60.98971 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f13abf5-fb26-3050-91c4-bb6316e1a49f | -10.41968 | -60.99449 | 2024-10-09 05:04:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a0e0ff42-502f-380d-8035-f5bcef2f1b4d | -9.91991 | -60.32014 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11543a82-a001-39ff-ab2c-87e260490f53 | -9.91695 | -60.31504 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ccd5ba7-b189-3f36-9ae5-5d31ea30ba2d | -9.91619 | -60.3195 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06cc3e61-389c-398b-a769-0b7be0aea6fc | -9.90658 | -60.30857 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bc0ccbf-ee54-354a-bcf3-24fa31bf2e52 | -9.90286 | -60.30795 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07de7652-e85a-375d-b6d0-2fbf344e7b6a | -9.90208 | -60.31248 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 426aa743-0fc4-3228-8fbc-ade98bf11cdf | -9.89694 | -60.21762 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 621a40ed-78ea-3bd0-9839-dce7495c3071 | -9.89619 | -60.3022 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9525f73c-d40d-3059-a6ac-25cce194fc64 | -9.89406 | -60.30433 | 2024-10-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README180.md)
