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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a72a0679-6cf7-37d1-adfc-b5d8efccbb4d | -2.93187 | -53.70108 | 2025-08-24 04:57:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 878edeb4-5054-3d9f-9ee2-054ae757a64a | -5.41352 | -44.98655 | 2025-08-24 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| db8528aa-c294-3fae-b898-45f8ea61a258 | -3.32073 | -48.71072 | 2025-08-24 04:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed46bcbf-fe27-308a-8fb2-b8fa0e9969d6 | -1.55528 | -54.54435 | 2025-08-24 04:57:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| accb3c46-df00-3cd0-bcbb-d88fc9e42f39 | -3.1376 | -58.03675 | 2025-08-24 04:57:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fc8f8a1-7268-3710-8ba9-bb3f7960b31a | -5.41305 | -44.98982 | 2025-08-24 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca08db99-cc61-3c29-b7b3-fc8eb769382f | -7.31567 | -59.61439 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ce1bda1-8017-3756-839e-024d8b18e78f | -8.75153 | -46.74182 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc71272c-fbfc-3ad9-9099-da58dc0e2567 | -8.75151 | -46.71627 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b81c3ef-97a1-3c6e-94cc-569d91afab10 | -8.06151 | -44.98237 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbdea576-614f-39a7-8a9c-d7e9c4ba5183 | -6.91376 | -52.8535 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e54a83e0-4dad-316a-846c-9150a7c4b682 | -7.94631 | -63.05659 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a2ae745-07be-38f2-a0ac-53facf1353d7 | -9.14757 | -59.49318 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 989df06b-fe22-33af-b839-a63ec6f37e04 | -9.23115 | -61.02858 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd4ca66e-f0b1-35ad-b475-839c6e4c9b6c | -9.14896 | -59.4751 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4a186c4d-5fbb-3b9e-86ac-5fb64e996203 | -8.14195 | -62.87409 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 150732b1-726f-3ddd-b88e-1dad4c40ab10 | -8.13689 | -62.87316 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f0e4884-d6a9-3ef3-8227-ff37fdc6e5ee | -11.13975 | -46.33343 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcf29ebf-59f9-3a83-9099-02eba88a7496 | -8.80459 | -48.78189 | 2025-08-24 04:59:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 981bcdf0-4bf4-35f2-a813-7f657e9dd21e | -8.8413 | -49.8978 | 2025-08-24 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c81f9d6-e1aa-3300-8421-ba9393a17f87 | -9.24821 | -48.19681 | 2025-08-24 04:59:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9301804-bbe1-3a5b-8b8f-fb6ae3ffa36a | -9.19487 | -59.62332 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddcee86e-ad1d-31b3-95b0-179a218fa2a4 | -7.54759 | -63.8602 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5610a62c-3f2a-3105-94eb-f8576167cfef | -9.16616 | -59.48045 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d39f3ab7-b56e-3a7d-b896-199292d0d336 | -9.80267 | -46.4188 | 2025-08-24 04:59:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 983c4db6-e960-36bd-af64-0081382ee1ec | -8.13851 | -62.86428 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9de0d8eb-ebf0-365a-808f-c409255ed869 | -9.16397 | -59.48304 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| da0a317e-46c7-3528-8e0d-a3c0c01538e9 | -5.80866 | -59.21138 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3349938-7faf-3ad8-b84c-819417a8f75a | -10.6033 | -44.3236 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a85fbe05-50b2-33c9-8ce2-bdbe5b2b80bf | -9.2165 | -59.61727 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e94e7c9a-ae95-381d-94c2-871c762eb2b2 | -9.20671 | -59.48229 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaa0f818-74a7-3b5e-8abd-9a1565501e79 | -7.54889 | -63.85313 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 886fd416-32e2-3e2e-a5ce-6665c346085d | -9.16091 | -59.4637 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 78b48a0e-3a53-3cad-a49f-a1ad2ac09a71 | -8.19007 | -45.10324 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 786cd735-3ec6-3b37-9396-b516defa49c9 | -8.91151 | -62.42299 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9bcdef6f-f671-356f-8b7f-f36513a88151 | -7.5585 | -63.86227 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e36b274-5f8f-3e0a-8221-773b82da39a6 | -9.17339 | -60.769 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46131a28-ca6a-3919-b15c-401c8183ff30 | -8.88049 | -62.42844 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e1d8749-731a-3498-b24a-b66cd7224c57 | -8.18557 | -45.09559 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31d19198-8646-3bf2-ae5e-495758a41615 | -8.90279 | -62.41583 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3adeb20-8917-38ee-963e-e92ed9024c10 | -8.84162 | -49.90574 | 2025-08-24 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae3a2d59-71a2-3b1d-9326-e41c7df16b55 | -9.15913 | -59.48754 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 672200d2-0260-39fd-b7ab-1de1ee764c52 | -9.82017 | -46.44296 | 2025-08-24 04:59:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a2dd8dd-c051-3ee8-a3b0-880746719088 | -9.19251 | -59.61301 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2407570f-44fb-32f5-b02c-c66f0fa18b65 | -9.19746 | -59.4648 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eeeec95a-5bd9-3a8f-bf4d-ff6149e970d6 | -10.47655 | -46.88595 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f53e714-067b-3f37-af68-8351893d2075 | -10.81091 | -46.41312 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b868e5a-0986-3f75-b8c6-b6ebca191471 | -10.80652 | -46.40617 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc3b2fb1-9882-3377-8fad-f7940c0a7128 | -9.16398 | -59.46949 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7ea824de-a593-3be3-aa80-e8f2c7658fc5 | -9.2043 | -60.79571 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81354f82-222c-3129-98f6-1699fa243fba | -11.14017 | -46.33024 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd111f9f-324f-350f-99b8-433ce3d6c66e | -9.25267 | -48.19749 | 2025-08-24 04:59:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 715c4d30-41ad-31fe-87db-8162427b0823 | -9.23539 | -60.92624 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3eade94a-fe15-33ff-a860-86fc4dff26c8 | -9.19999 | -60.76948 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 986b83d1-ac09-3769-aee3-84b82c446bda | -6.87291 | -59.82445 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a763b315-05bb-3e02-b83b-df3f30807747 | -8.8902 | -62.40246 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd3cc310-cac4-3211-9e2b-ddd1f309b2c8 | -7.55434 | -63.85415 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adec63f8-26eb-3346-b02e-c29d9c2004d7 | -8.53545 | -48.86354 | 2025-08-24 04:59:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03620106-644f-34b0-9a1b-ebdc99cc1cc7 | -11.13933 | -46.33662 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83e44fea-73b2-3e54-bdfe-dd73f26a29b1 | -9.18558 | -59.46268 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 217370e6-d182-3e87-b943-68023f243d78 | -9.13616 | -60.77181 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 751d53ba-d84e-349f-b87f-8debb9e022dd | -8.74517 | -46.72632 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8bbdb771-3a79-3730-965c-462a9ee8b382 | -6.688 | -58.8544 | 2025-08-24 04:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f8882fb1-8f51-30f2-856c-e27429289067 | -9.16972 | -59.45997 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d415ea0b-e961-3b81-a227-1f158a027d71 | -7.94007 | -63.06179 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35ee0f95-3691-3c3f-8fad-ac7ae8bbbf28 | -9.23108 | -60.92809 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57fadf34-2149-353c-8771-91410636c357 | -6.92336 | -62.91 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dc0c656-6d05-380d-8f1a-6b0b5733fc63 | -8.75841 | -46.73952 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc2a9ee5-9ff3-3811-b61f-7903d19968de | -8.70618 | -62.87962 | 2025-08-24 04:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a49d6172-b380-32dc-8e96-b6a38b89a865 | -9.1876 | -59.61759 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c320c2be-5ccc-3d44-b23d-a63747e1fe47 | -7.78642 | -61.57598 | 2025-08-24 04:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8a118e2-a6cd-35c2-a8de-66844749682e | -10.81752 | -46.39007 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e5883df-ec3a-3ce8-8e18-de61542cc248 | -10.41258 | -47.18213 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3758c6a-afeb-3aeb-b8ef-cf68bf5024c2 | -9.17765 | -59.46133 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0e44de80-9188-36a9-9a44-011971939ca1 | -7.3163 | -59.6107 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3281ddd-be92-3eef-926c-429a88db21ce | -10.82304 | -46.40027 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbfba9fa-2459-334c-9723-9be91b899071 | -9.15741 | -59.49782 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cf22c4ab-03bb-3d4e-b46a-619b77b7cd8f | -9.14847 | -59.48805 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5d8daf96-7500-3ecb-ae38-830462258d75 | -8.68111 | -62.87973 | 2025-08-24 04:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c5798d69-d717-3f90-8e91-fe016c845178 | -8.61736 | -62.60118 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3aa02d69-7136-3aa8-a424-d4bd392f4a7d | -7.02683 | -55.43576 | 2025-08-24 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3fdc7cdb-f11e-34fc-9773-72ee9fa7cc56 | -7.02626 | -55.43934 | 2025-08-24 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 667dc658-093c-3a92-b071-00b85726cc06 | -10.80834 | -46.41946 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26bcf239-345f-3834-b9e6-92f91482e1c3 | -8.14103 | -62.86288 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8ca3788-65bc-34bc-9c7e-c90f0ab2034c | -8.6075 | -62.59933 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bfa4871e-2075-3ed7-99ed-919d09bf9aa7 | -9.1935 | -59.4641 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e4817b9-8cb9-3113-8bf8-6bf2a0614566 | -8.11034 | -47.14415 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b5afeef-679a-3a63-ab8b-bdf978b06d03 | -10.57994 | -47.14014 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5d6a4c3-3e73-3cb7-8a58-b322dbe4a2c3 | -5.6119 | -60.22605 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4a9d54c-1874-3462-970b-e425be1b64f3 | -8.92467 | -60.71944 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ea1a424-384d-3142-943d-5da26c12b354 | -8.60983 | -62.59034 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1dd5af15-f109-3378-8358-705abfb630d2 | -9.68335 | -48.34609 | 2025-08-24 04:59:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 006619df-e22e-394d-8c46-2540a6b0053c | -6.9239 | -62.90688 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b04b3977-c785-3b56-b1e5-6b8813ca1d81 | -9.16173 | -59.47203 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dadc3b3b-d5fb-3c18-abd3-e40f198a4482 | -9.25437 | -60.92346 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c79dafc4-ff03-3394-b307-f9d90880549f | -9.17119 | -59.5933 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be5bc7ac-b920-31c2-a0f8-dd2d9897af60 | -9.81468 | -46.44529 | 2025-08-24 04:59:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09a749b4-292f-3b14-9aeb-ad8853888637 | -8.68613 | -62.87587 | 2025-08-24 04:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20cf1439-3e40-3c6d-b189-3574e910176f | -8.53967 | -48.86421 | 2025-08-24 04:59:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 046314fc-4adb-38a1-98a6-db394226e14b | -11.11599 | -44.78921 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README54.md)
