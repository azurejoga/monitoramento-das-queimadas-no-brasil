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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 760aea89-b77c-3cee-b2fd-ebb0e3caad0e | -13.3537 | -54.4213 | 2025-08-19 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 187.6 |
| 31f7e8bb-e8c9-36d0-9fed-8c8b8ee89286 | -6.9527 | -43.585 | 2025-08-19 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 168.2 |
| d2a1ed0e-3a12-3eaf-8a94-6d5f10ce653f | -6.9715 | -43.5833 | 2025-08-19 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 338.4 |
| d5b04d09-3ca0-32fa-9705-8c8af6c4ffd1 | -15.0196 | -54.8112 | 2025-08-19 13:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 1f388f61-a256-3fe8-b5d3-f748d27e9e9b | -12.9925 | -45.202 | 2025-08-19 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.5 |
| a43a37ee-037f-3f8d-8797-6b9c35be1a3b | -6.5201 | -45.5013 | 2025-08-19 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 155.5 |
| ef445070-ecc3-3904-ac73-c2a1517b0457 | -12.5042 | -45.5788 | 2025-08-19 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 0584d26e-c8a2-35d4-b33e-13f3ba3a083a | -13.0119 | -45.1988 | 2025-08-19 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 374.5 |
| 978f6f21-4060-352a-a9c3-7b41fe14647c | -12.898 | -46.1135 | 2025-08-19 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 87b63a85-f0ea-3cbe-97a5-38a87424f284 | -6.5013 | -45.5028 | 2025-08-19 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ab6e68fa-90d3-395d-8c39-d7567a5c6e76 | -12.4729 | -43.1967 | 2025-08-19 13:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 3b5b8171-200e-3369-9726-698faf2a66eb | -13.354 | -54.4006 | 2025-08-19 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 30e427d6-7f80-3b95-b67d-f8e54652dcee | -12.8984 | -46.0906 | 2025-08-19 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 204.6 |
| be9373ce-ccb6-3dab-af15-011431d9e3aa | -6.9339 | -43.5868 | 2025-08-19 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 7553999d-3032-30fb-8273-65574e090341 | -6.9712 | -43.6066 | 2025-08-19 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| ec49623d-4f87-3f67-85fb-177b4d369242 | -13.8748 | -45.5411 | 2025-08-19 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 3e01e093-4846-349a-9eac-8452b1305135 | -6.5199 | -45.5238 | 2025-08-19 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 2b3d6a5b-a1dc-3ee9-b1d0-4ee0a76c18ad | -13.3534 | -54.4419 | 2025-08-19 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 0d6cce1a-09a3-3a1d-a91c-82f32d924688 | -13.1746 | -54.9337 | 2025-08-19 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 8c0fdca4-ac93-33c3-89de-34076525c903 | -13.1555 | -54.9357 | 2025-08-19 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 311.3 |
| c7f2ea8e-7e57-3e5c-8d92-6c8ec0863001 | -12.8984 | -46.0906 | 2025-08-19 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 3114967a-c617-3d00-85cb-c69fa09776be | -6.9339 | -43.5868 | 2025-08-19 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 149.2 |
| ef034de4-035d-37ff-b998-4d1f4069c363 | -15.4581 | -43.6408 | 2025-08-19 13:40:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 002f687e-cdfb-392a-8e93-17f66d978b98 | -12.898 | -46.1135 | 2025-08-19 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| ef09b970-78ef-3708-9e4b-49b213ef579b | -13.1552 | -54.9562 | 2025-08-19 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1a069e57-20b1-3858-bd67-b93dba499518 | -12.9925 | -45.202 | 2025-08-19 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 6293f76a-5824-339f-8929-75363f6d3c88 | -6.5201 | -45.5013 | 2025-08-19 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| d55bc37a-6456-31c6-8579-18cd6632181c | -15.0196 | -54.8112 | 2025-08-19 13:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| e586ad3b-4e93-31fa-9db4-2cd2339d3135 | -15.561 | -50.5348 | 2025-08-19 13:40:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 673c9179-11bc-3bb1-a945-9cabf79b9eeb | -13.3537 | -54.4213 | 2025-08-19 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 166.7 |
| 71dc0938-f2bd-38e6-ac3a-a535a21d9699 | -13.1746 | -54.9337 | 2025-08-19 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 221.1 |
| cd16bf2b-c011-34b1-ba79-59a95bba6e47 | -6.9715 | -43.5833 | 2025-08-19 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 16a0e856-db4a-351d-8210-dd6f15c81491 | -6.9527 | -43.585 | 2025-08-19 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 23cbe987-8c22-33f1-8cd3-7a7407f62d8a | -12.5042 | -45.5788 | 2025-08-19 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 236.3 |
| a806ee56-0367-3671-8f0c-cf543b9768d9 | -13.354 | -54.4006 | 2025-08-19 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 869a13cc-cb0e-3f0f-a4e6-7d9250fa3d40 | -12.4849 | -45.5817 | 2025-08-19 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0b85a499-353e-3c34-9884-1eb5e6f48aac | -12.4729 | -43.1967 | 2025-08-19 13:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 1a7f37cf-59eb-3b09-aeb6-ca092c0f94af | -13.1558 | -54.9151 | 2025-08-19 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| ebc79e82-eef8-396c-861d-5ed927cc1889 | -12.9739 | -46.1703 | 2025-08-19 13:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a4cd6390-a6be-3d16-ac84-14102b7ea906 | -13.1743 | -54.9542 | 2025-08-19 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 2aadfa1d-ad28-3627-9134-da0ac3f89b1c | -13.0119 | -45.1988 | 2025-08-19 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 341.3 |
| c347ca26-7cd9-34fc-a6d7-6a543e455b48 | -5.7887 | -43.6134 | 2025-08-19 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 0b941d8f-a780-3c41-8cd1-a03e6a3ee630 | -14.1707 | -45.3042 | 2025-08-19 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 4b44b8f4-329e-361c-82ff-8ee1262adaa8 | -6.9712 | -43.6066 | 2025-08-19 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 7fa722bb-85fb-3491-867f-d4ca05d55649 | -9.3395 | -48.5234 | 2025-08-19 13:40:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| f2085e3c-fc68-3a9b-ac9d-3804470c52c2 | -13.1555 | -54.9357 | 2025-08-19 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 458.2 |
| 9d48ac9b-073f-3b68-9719-5063924f6628 | -6.5199 | -45.5238 | 2025-08-19 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| edae487c-16d1-3550-9557-1a1abfc7437f | -13.3537 | -54.4213 | 2025-08-19 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 230.9 |
| 3d8f226d-e67f-3535-ba8b-e6450e58f1a2 | -12.9173 | -46.1106 | 2025-08-19 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2e7cb0c4-c0bc-3646-a1ab-5d1f51a802d3 | -14.1707 | -45.3042 | 2025-08-19 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| bab1ea28-5cec-3d9e-8099-731d094cbdf3 | -6.9339 | -43.5868 | 2025-08-19 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 67bd0f3e-3fe9-36c6-a272-f46cf6edad62 | -12.5042 | -45.5788 | 2025-08-19 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1102796c-211c-3cea-be9c-722829329d29 | -12.8984 | -46.0906 | 2025-08-19 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 9154d053-2afc-3b12-8757-1944392660d5 | -6.9712 | -43.6066 | 2025-08-19 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 00d022b6-687e-3bbb-9206-e7b965ca34e1 | -9.1709 | -59.6374 | 2025-08-19 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3fefe611-c091-3690-824c-57a447d80ed2 | -5.7887 | -43.6134 | 2025-08-19 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 3985ab33-8f2d-3695-b17a-d2250c4dbc88 | -10.9916 | -45.6359 | 2025-08-19 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 437214d1-3a6e-3832-b891-547b4e157364 | -6.9527 | -43.585 | 2025-08-19 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 4726bb1b-9c1b-3201-824f-ea888da990a5 | -15.4581 | -43.6408 | 2025-08-19 13:50:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 137.7 |
| 1b93b432-a55b-31d8-9f36-b1610c3d8964 | -12.898 | -46.1135 | 2025-08-19 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 202.5 |
| db1852a0-7726-38ec-9783-e03983f85916 | -13.3534 | -54.4419 | 2025-08-19 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 12d37e8d-b5e2-3b83-90f6-a2f7b702b8b2 | -13.0119 | -45.1988 | 2025-08-19 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 286.7 |
| 1e472a12-4092-35d5-bb70-299ff9d88aa9 | -15.0196 | -54.8112 | 2025-08-19 13:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 64266225-3e25-3c39-a1d9-e9416d27fc76 | -6.9715 | -43.5833 | 2025-08-19 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 260.0 |
| b247e67c-fe80-3888-ad77-aa344072b96e | -6.5201 | -45.5013 | 2025-08-19 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| ba0d09f3-553b-327e-98ce-eb1dec940d50 | -3.982 | -42.516 | 2025-08-19 13:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 6624923b-37d0-3a91-a19a-2d53a5f38420 | -9.1895 | -59.6364 | 2025-08-19 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 134f5b49-62fe-3614-900e-c1d0de22bad9 | -9.1898 | -59.5977 | 2025-08-19 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| a10156e9-e19c-35da-a8a0-e93e776bf342 | -13.354 | -54.4006 | 2025-08-19 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| eb2238ec-54ec-3d2b-b950-efc0bc4f15b7 | -12.9925 | -45.202 | 2025-08-19 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 176.8 |
| c317cb5a-0e4f-3aec-b5f2-5863b4d3258b | -6.9339 | -43.5868 | 2025-08-19 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 6486dac6-284c-330e-8cb9-aa83b3cf30c5 | -6.9527 | -43.585 | 2025-08-19 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| af1c882f-c0b4-33e3-9fde-503ea99f1a21 | -9.1708 | -59.6568 | 2025-08-19 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 5f14ce71-f360-3c7b-893b-a4b1e8c23fbf | -12.9739 | -46.1703 | 2025-08-19 14:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| d720db7d-b0be-3174-be7a-ce621224ecb4 | -13.1558 | -54.9151 | 2025-08-19 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 143.3 |
| da6a2a58-98ed-3616-b061-6bd541ad5781 | -13.1552 | -54.9562 | 2025-08-19 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 5e503576-6ad1-3df8-898b-5d915ceb0adb | -15.0196 | -54.8112 | 2025-08-19 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 7924d28a-98df-3b4d-bd07-1c6de992d101 | -13.3537 | -54.4213 | 2025-08-19 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 233.9 |
| d57cda56-ceb1-3b1d-85a5-64d15d51031f | -13.1555 | -54.9357 | 2025-08-19 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 502.6 |
| 310d7a83-2219-353b-b0c8-57f721ab52ff | -9.1895 | -59.6364 | 2025-08-19 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| dc6451f4-081c-3539-b96e-06a00be0ac61 | -13.3729 | -54.4192 | 2025-08-19 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 180938e1-06f7-36f6-ac98-9ff6c906caa0 | -13.0119 | -45.1988 | 2025-08-19 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 310.8 |
| b3fa0085-d0b0-3794-b0bd-2d5308e04b02 | -9.1898 | -59.5977 | 2025-08-19 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a6e0dfde-f725-3faa-a67f-7b6631b141d0 | -5.7887 | -43.6134 | 2025-08-19 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 11f73ab1-4922-3038-b90d-809f202b099b | -12.5042 | -45.5788 | 2025-08-19 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 7f19e5cc-4a11-3241-8c76-c55313613238 | -12.978 | -56.8413 | 2025-08-19 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 58148ebf-5bcd-3760-a65a-e5597e4308db | -6.9712 | -43.6066 | 2025-08-19 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 50b06e6e-e6c8-3c98-9057-4c0183d84d47 | -6.5203 | -45.4787 | 2025-08-19 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 8cd2b9b6-d5fb-34c8-87ea-e5531e31e263 | -13.2567 | -50.7947 | 2025-08-19 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 37d19210-d2f2-33de-a74b-2fff41516984 | -6.5199 | -45.5238 | 2025-08-19 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b972d9c7-21a5-3adb-a592-36511e7b9631 | -12.898 | -46.1135 | 2025-08-19 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 5b2f91f8-3dd1-362a-9894-ba92e88f21ea | -6.5201 | -45.5013 | 2025-08-19 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 195.6 |
| c5d29563-a79e-3664-ab83-7aab0493defc | -12.8984 | -46.0906 | 2025-08-19 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 00361dfe-1aea-33bc-a938-872f932238de | -13.257 | -50.7732 | 2025-08-19 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b861f814-3fdf-3d96-96f3-85d9966f2395 | -13.354 | -54.4006 | 2025-08-19 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 9776cc99-d588-3dd6-9074-47353eda24d6 | -12.9925 | -45.202 | 2025-08-19 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 258.0 |
| 4693a564-c3b9-3e5f-a081-34f68bab135f | -13.3534 | -54.4419 | 2025-08-19 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 5eab8922-7a8a-30f7-92cc-13c1812e4ffc | -9.1709 | -59.6374 | 2025-08-19 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b712e602-3e08-33a6-a7c9-f7d8941ae292 | -14.1707 | -45.3042 | 2025-08-19 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 3150f634-066a-3649-8177-d88a8757607f | -6.9715 | -43.5833 | 2025-08-19 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 248.3 |


[Clique aqui para ver as próximas entradas](README60.md)
