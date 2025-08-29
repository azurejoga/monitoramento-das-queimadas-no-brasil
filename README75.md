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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c102c72-287a-3f18-8b62-bec898a29849 | -9.12093 | -65.77032 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 347fd854-194e-3568-865a-d24d2dd81143 | -11.56293 | -47.61869 | 2025-08-29 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47f23db7-e62c-37c5-a414-7f69e9887a9f | -10.85668 | -47.4966 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90a3064a-ed3f-3cc2-9280-652cbd193b54 | -12.84791 | -48.09942 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9854fcbc-2f15-3769-9343-e3bf02c9abfe | -12.81691 | -48.17501 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf316374-119a-3003-8137-fbecaae0d7d0 | -12.85231 | -48.0994 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3210da7-f325-3c27-85fd-45a4588266ca | -12.9096 | -48.11464 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48dcb422-4d05-3e3e-8c44-d54833896735 | -15.66311 | -52.76452 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcb7a50d-1df9-380e-b21e-10fedb923c56 | -10.98037 | -46.90876 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d1c74d99-292a-3c21-8459-9402c94dfd36 | -13.4229 | -46.97736 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| bc38ca13-68ac-34a7-bc37-cde5b1ab9d28 | -9.78092 | -64.25889 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 88934c23-629b-3412-8754-5b9c78e8cf9b | -13.39954 | -46.98977 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80e01142-46e5-3093-aa44-906bb341a7dd | -11.3801 | -63.27358 | 2025-08-29 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a75affea-4a00-30eb-b708-6f21d42cd117 | -14.79032 | -59.72085 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f17277fd-753f-37d7-8dac-ba8a468cc494 | -13.00991 | -56.9186 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de65dba9-315b-3f57-a074-a014238dcb4f | -8.13956 | -61.21355 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 77f1a95f-a833-3c6a-8570-c1c4bde563f5 | -9.18109 | -60.86132 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a415f05f-20a1-301c-b49c-e4abb94067b1 | -13.54048 | -46.88406 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efa60e8a-e546-32ae-84e5-bbc955dcbb73 | -12.69157 | -48.16002 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c16030c2-8892-39ff-8234-2aab05692f96 | -12.63079 | -60.25224 | 2025-08-29 05:08:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99a5a759-fed2-3492-a7a8-2837dd356f4c | -9.16788 | -56.99449 | 2025-08-29 05:08:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4919c18d-9cfe-3c44-a41d-82433260042e | -13.41108 | -46.9788 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d50eb059-86df-3cc1-af63-5b306cd2bfdf | -11.34926 | -43.55194 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 947ec59e-49b6-3b8b-b1d8-e132e9d94bfd | -13.54244 | -46.86792 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe4865c5-fd54-30c1-b584-e1065b38f56b | -12.43444 | -63.92186 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 47284044-ac7b-3e77-8ae4-9989f5326741 | -10.3748 | -57.83042 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a2a1755b-2dbe-37e9-9199-70d086f8ae3b | -13.39909 | -46.99371 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f5b33168-742d-33b0-a432-b7ddca8fd66b | -12.69278 | -48.19311 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 85b858ec-70d6-351e-a393-36cce51de736 | -11.88208 | -46.39816 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 171edf56-8e02-3d33-a0c1-194799314266 | -8.18072 | -61.38179 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f20e3221-ab68-360e-81cd-9cf4b726d092 | -15.53312 | -54.2683 | 2025-08-29 05:08:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eafd644d-efda-3a60-9c7e-e78a0962bb7a | -10.83439 | -47.50034 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0dcca66-2dcd-343f-9de2-09566ae1ad2f | -13.55162 | -46.88721 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d8806e38-f071-378d-87ac-8f33903e791f | -12.99217 | -56.90115 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24e6aa25-e9d0-38ae-b148-21c0bcbe54b3 | -8.95862 | -65.97195 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3caa2ab6-11f4-33d9-a9af-1c264bedb7de | -13.41222 | -46.96931 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c4044c2-d666-3df0-affb-783b4dbe7ef6 | -13.58927 | -46.86634 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d64df86a-1021-35eb-88e1-519fc67f8b2a | -11.94434 | -46.7108 | 2025-08-29 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bcee8d1-f679-33e8-bbb4-9f358cb02dde | -10.47049 | -57.93149 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a73aa5b3-ca54-314a-8f64-c14dcb7f5b10 | -13.01437 | -56.89021 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b6f9339-2f5e-312e-a43e-18cdcfb0c930 | -10.86078 | -60.81112 | 2025-08-29 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 650b5d7e-ba6f-3edb-850c-4f3f9fc21fdb | -12.82856 | -48.16755 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a21fa9a-d79f-325f-aab2-3588535734bb | -9.11475 | -65.74364 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d377dd7f-8bfd-363c-bdd0-42be7411ee8a | -10.85133 | -47.49573 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90889407-2a37-3584-93ba-9fadad5124c1 | -10.12028 | -47.43322 | 2025-08-29 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b699574c-dd4e-3941-8a4b-abe8daefd597 | -15.0406 | -48.13307 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1640ec1-30a3-3c74-86ef-49972b607dd9 | -11.56785 | -46.37823 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5be1624e-23f1-3c5b-b7de-fd2711eccabb | -13.36743 | -51.76517 | 2025-08-29 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a12852ee-b777-313a-8104-28dd61868e5f | -15.31986 | -48.22534 | 2025-08-29 05:08:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3957589f-3a11-3df0-8dc3-cffa7f1c11c7 | -10.61479 | -54.90665 | 2025-08-29 05:08:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cccdff93-ac59-30b8-8168-c33b7f26f81b | -9.55442 | -63.21218 | 2025-08-29 05:08:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 007dac63-0369-38ea-a489-d00a406c1612 | -13.41009 | -46.844 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ab91602-dff6-38af-bf15-8ce009da8f99 | -12.32592 | -47.05069 | 2025-08-29 05:08:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad628e40-cfe3-329b-9b2a-9cbabc9e98b7 | -10.94367 | -46.85688 | 2025-08-29 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2ccd9c7-169c-3e2f-b035-24744d2a1697 | -9.45288 | -60.55833 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 583e2d09-c7ce-3a0e-82ca-ed9cd88f96b3 | -13.54576 | -46.88713 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c19be50-3f0b-3a83-b5dd-196a048f7186 | -10.48332 | -57.96293 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1de60257-437b-360b-8856-00ad27f118e4 | -13.62083 | -48.24586 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c252df4-8664-3ecf-b26a-375b8af2cab3 | -9.93848 | -46.71476 | 2025-08-29 05:08:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cd51839-37fb-3e4a-ba80-c2d41d2a6151 | -12.92803 | -48.13919 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 239a01ad-630a-3321-bde0-99f82777c254 | -12.44063 | -63.9135 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40757b7c-26c6-334a-b103-4a0113635837 | -9.52629 | -60.51031 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ce39f14-1b7d-3d1d-8698-f44b04087114 | -11.56247 | -46.37367 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd1b9c55-3cdc-32b8-b267-58e2c7d9d2f3 | -9.44986 | -60.55289 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| d4096b10-286d-3fa9-9d14-b9074c8f1507 | -13.40683 | -46.96571 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 841e0cd1-6ffa-3764-b54b-a423da00b286 | -12.69314 | -48.19021 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee0fd026-af1e-3cc7-a779-bca98decfaee | -9.12505 | -65.77825 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b955e67-9366-38c3-827c-0645507248be | -10.45393 | -57.96977 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8837465b-6337-3069-bff9-01d776179d36 | -10.9842 | -46.89579 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e97ed016-eb12-30f2-a6ed-e9146f57183c | -10.80611 | -46.35829 | 2025-08-29 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4a94f57-4331-34eb-9006-2e9513f617a7 | -11.57567 | -46.27052 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3df72e3f-c913-31fd-9116-15c94d852120 | -12.7067 | -48.1873 | 2025-08-29 05:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d41074c3-021e-3ed3-9ef4-c2ecf63622fa | -13.5386 | -46.8775 | 2025-08-29 05:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a2ff041d-a99f-377d-8f1b-f4db5ab316f6 | -9.4432 | -60.5692 | 2025-08-29 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0c79c703-351d-3f5b-800f-74233b55dce2 | -3.4254 | -49.0517 | 2025-08-29 05:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 58274871-758f-35ce-9098-5f5844ec9173 | -8.1758 | -61.3755 | 2025-08-29 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 170282de-f5f3-3e65-8f4a-d21f25af11ba | -9.1154 | -65.7886 | 2025-08-29 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3dfde7fb-4169-3e2d-8e53-08b99bb51e69 | -10.9709 | -46.9266 | 2025-08-29 05:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 3bff2ab1-e760-30f6-a89b-2a36e381f5d3 | -9.4433 | -60.5499 | 2025-08-29 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4f0afa95-532c-3c3e-a7c8-9ffee3faff58 | -9.773 | -64.2469 | 2025-08-29 05:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f0b46b36-083f-39dd-b1db-a0a64b7825db | -13.4208 | -46.9864 | 2025-08-29 05:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 84cdad37-f726-389f-a7c4-795bd4f98351 | -13.4212 | -46.9637 | 2025-08-29 05:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| fe4834b4-ba82-3ae3-b479-b87ff38d772a | -9.462 | -60.549 | 2025-08-29 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 1d997b13-0828-3d3c-a873-9ffdf9e71774 | -12.6875 | -48.1899 | 2025-08-29 05:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 634e943d-2640-33a0-98eb-0cffb48fca22 | -9.4618 | -60.5682 | 2025-08-29 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 0dcc2e7a-ad29-33b2-8617-23e92b4fdd59 | -9.7728 | -64.2657 | 2025-08-29 05:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 4658389e-ac9e-33ed-aace-917ee7ce3015 | -9.1155 | -65.7699 | 2025-08-29 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| ccb08eaa-8d1e-39d4-9a0f-865cc130ec9c | -9.4949 | -45.3906 | 2025-08-29 05:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 737f1dec-fe43-3094-80f8-f15ea7751e04 | -18.19683 | -45.59471 | 2025-08-29 05:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be3b57a1-01d7-3882-a852-6dc119941fdf | -24.16498 | -49.57274 | 2025-08-29 05:10:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 63288570-cc7e-3964-b38f-cee46882ba24 | -17.54539 | -46.60929 | 2025-08-29 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a977b5f7-91bf-3966-abc0-3f55a1ab0a90 | -24.16464 | -49.57656 | 2025-08-29 05:10:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1026ed79-517d-3967-9d28-105da2fa953e | -17.5403 | -46.61296 | 2025-08-29 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 120ee099-f5a4-3af4-b5ad-75b344a370c3 | -18.18806 | -45.59842 | 2025-08-29 05:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c367dcc-5b8e-3e20-9622-2ddff6f3b554 | -17.53931 | -46.62278 | 2025-08-29 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f43cdc0-a88b-3d27-a320-caae4434d2d9 | -24.17128 | -49.56487 | 2025-08-29 05:10:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8166e014-c5b7-31e7-a835-775fa6fa5696 | -24.17017 | -49.57728 | 2025-08-29 05:10:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 05d5b333-35e0-3215-9627-d332d7bbd11e | -17.53881 | -46.62769 | 2025-08-29 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f981f70-1bec-3fe6-ab95-2108ddcf223b | -24.16572 | -49.56451 | 2025-08-29 05:10:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b19281c-5e7d-361b-9129-146d950d5e29 | -18.19511 | -45.59422 | 2025-08-29 05:10:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README76.md)
