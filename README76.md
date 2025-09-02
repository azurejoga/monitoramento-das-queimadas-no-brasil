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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f475b4f6-a4d1-3f30-b988-aac5eebcfa69 | -6.82614 | -52.81758 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07d9a27e-9280-3740-9284-8182458e3931 | -7.97212 | -63.66375 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f89a728-fd6c-38d5-a923-604f8a17b5b0 | -10.2516 | -64.49717 | 2025-09-02 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7f1b5d1-9b79-3671-afd2-02187a652f98 | -8.66947 | -62.83356 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3df0d374-47b9-3884-b0d5-f58c3375e05b | -6.75626 | -56.39368 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 538ba469-ad68-3fa6-b2c8-bd5a50184d6a | -11.67802 | -52.18975 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 5e6aee41-df22-3739-a460-71d49967cc74 | -8.72565 | -62.41306 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d0a42de-75e6-3f80-b395-4020d266a8ec | -10.76178 | -59.83861 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e29f1624-a2a8-3cfa-9301-b58e6c5972bc | -8.69294 | -62.40428 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10a90cc4-d76b-34fb-a265-928a405c923f | -8.66614 | -62.83303 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 545f5374-124c-3f7c-96d9-9449247772aa | -6.83158 | -52.81832 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 578f31b6-43d7-3f7b-b580-347bce067a22 | -9.12387 | -65.76744 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 863c842b-68d4-3d94-9051-80e36fa9c294 | -7.96875 | -63.6632 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02f2c836-dea2-3d6f-99a4-1d800600e462 | -8.66226 | -62.83599 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 978f9d96-6e5d-3d08-9f50-4a32561971ae | -8.7632 | -61.43979 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 435bb164-91df-3afe-8a9d-bba84de37fc4 | -7.65985 | -61.09007 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80c22bd9-0d08-35c6-84c9-d31be277781d | -8.97352 | -65.97375 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2909f0e-ae17-3e36-adcd-a00847fea41c | -6.77624 | -52.81164 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a948757-6f02-3cc8-a640-15b7099966a7 | -6.79797 | -52.81467 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19a7b2ff-2772-30c7-a77d-f26778e5cc44 | -8.70902 | -62.41042 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 209d6ef3-a741-301a-b36c-ec80a9072b26 | -8.75439 | -62.42113 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bba0889-8dcb-335c-ad2e-f709c364dfc3 | -6.82023 | -52.82037 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 496f7158-bb5e-3d3b-9392-a7bc97d434f8 | -6.81791 | -52.83753 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d517a9c4-52e8-37cf-a869-a955ad957ec0 | -7.57536 | -63.05006 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa708ac7-1a29-32e7-b50e-734428e9516a | -8.65055 | -63.26916 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 985ce905-1813-38f8-b725-904fdc0bf2aa | -6.34764 | -53.43213 | 2025-09-02 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06d64850-156f-3192-a4bd-bf4d553efcf7 | -3.46016 | -59.86333 | 2025-09-02 05:31:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 038993a2-40f6-38a4-8f31-e99faa991deb | -8.85865 | -64.23098 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1095d26e-4a5e-341e-9bce-3a33ab643d07 | -11.64727 | -52.03716 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab73cc8c-b7a8-386e-8937-5ce7d9b3e5d7 | -6.86107 | -52.80538 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d02d1c0-9630-3d94-84f0-94587575c6de | -9.08885 | -59.48242 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d810344-ff01-3c8f-a910-1104f5c38b4e | -7.68064 | -61.08965 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6cf3a31-e2d2-3646-879f-0883b93a9aab | -11.9427 | -50.61612 | 2025-09-02 05:31:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed7e8593-607d-3326-8279-f76fea34ada1 | -7.27716 | -60.6501 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d71b881f-dc44-38b4-a768-9a1f14a8e0e8 | -9.72684 | -48.98736 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9cf506a4-e454-3092-b977-805e5289830b | -9.09025 | -58.89058 | 2025-09-02 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8a7f92f7-a266-3ab2-9a30-03984e85b011 | -11.65638 | -52.17904 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a49214e5-6060-3b62-a3eb-b49fab9d26a7 | -9.73843 | -48.98392 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd4d8168-f158-338e-bab7-13f097c59a6a | -7.70358 | -50.27153 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9d14d768-66af-36b8-952e-d0cd17ba1ec9 | -8.93443 | -65.94193 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9768157-c975-36ff-93f9-0e6f931a4859 | -9.43509 | -60.56286 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24335acb-26f3-3080-9d7a-70ad06abdf09 | -8.73676 | -62.42915 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03822406-781d-33b6-bb18-f2a27f52c842 | -10.44721 | -54.77575 | 2025-09-02 05:31:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 922df535-162b-3ab7-a2a3-cab31e41cf81 | -6.52642 | -56.20878 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5b1da04-814e-30dd-9f42-c02ad895eaa4 | -8.68574 | -62.40672 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6985ce2-1d8b-32c9-a8f8-d8bc44792681 | -8.75984 | -61.43925 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0d01e25-3a1d-32b1-97bc-821825e93822 | -11.67578 | -52.20786 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| db814f2b-35fb-3689-a314-91093935daf2 | -6.77671 | -52.80823 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 433241b6-64f8-3415-8d25-73fad376c480 | -11.67139 | -52.19371 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8e24674b-5dec-30b3-a142-6afe637ee56a | -8.73841 | -62.41867 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f23e637d-9edf-38f4-850a-f7fecad2f9db | -10.88482 | -55.75306 | 2025-09-02 05:31:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5188fef3-99df-3662-ada1-284d59cd4d6f | -7.54399 | -61.33895 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c65dd364-aae2-35e5-8bc7-d2e2ad2f93a6 | -6.80193 | -52.82584 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3797bce-cfb7-3934-8129-5946f7fab00d | -6.83019 | -52.8286 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf9e55f4-8252-3fdc-af47-4d20a432de4e | -11.42905 | -55.19111 | 2025-09-02 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14138505-4886-343f-bb35-37d7a36524e9 | -6.8182 | -52.82821 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d3e56d5-1162-344f-a92d-f2bec287fd50 | -7.36306 | -61.65376 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2ba7caa-e40e-3084-8dfa-62510f17da8b | -7.09399 | -63.03798 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae450e0f-6750-31bc-908b-babbde881698 | -11.67363 | -52.17555 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| cbab760d-097a-3dcd-83a9-68fa8dc051f3 | -11.66263 | -52.21507 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 57898074-44df-3a5c-ae35-6652488a464a | -8.67299 | -62.40111 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbd681c5-8313-39a5-ad66-04d1c2f26437 | -7.67334 | -61.09218 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e60a7a39-e5bb-3ff9-b0ac-1dff2761c944 | -6.82814 | -52.83617 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b63b48f-66af-395a-be3e-4f2c9a955b75 | -9.20804 | -59.53226 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3af94a5f-0c9e-3fe6-a57a-0090231e5607 | -6.8192 | -52.8212 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 312a5eb0-b970-3e1c-8689-8d588af3ba0c | -11.65276 | -52.19557 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1726a22f-4c9e-31a3-a148-3051e15e31e3 | -7.56474 | -63.85081 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fec0a6a7-45b9-3b60-b091-45d6ef5f0917 | -11.65483 | -52.19249 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e03a1ea0-0aed-3405-81a7-e57d7280198d | -6.84694 | -52.82758 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2330d6b-db9a-3387-ba7e-1b2fd08397f8 | -11.93383 | -50.60938 | 2025-09-02 05:31:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81c8ca66-d550-3e0c-b7f4-6a20357f9d9d | -8.75661 | -62.42865 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b3f6aa7-ff3b-3df1-b411-6b715ecd4bad | -8.70957 | -62.40693 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4639c200-95b7-3982-af42-a060ff341232 | -11.67137 | -52.20858 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 730ab7cf-c539-3127-a231-ea51256af507 | -6.43289 | -55.61864 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0c04f44-4202-3cbc-912c-f4642dfc4d9f | -11.66371 | -52.20628 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7714254c-63d6-3707-b484-394b0ff0b19d | -6.79941 | -52.8045 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6aea4a70-be06-3dd0-a5e4-4d86cdd336b8 | -9.31606 | -59.20731 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ea134e7-6117-3ba7-b8fa-296c7fcf8235 | -11.65742 | -52.16996 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f86c9222-b9d8-3d00-8a2e-1c384d7a92eb | -6.8143 | -52.8233 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c26af85-54d9-3f25-8fa6-39c6f9a93982 | -8.85501 | -50.58496 | 2025-09-02 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 121e60f3-0673-3b79-9cff-3823bf004c42 | -8.75994 | -62.42917 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdee84cd-2e8c-3380-8745-abe1582c1df5 | -7.60033 | -61.62955 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca9cfe73-47d7-39f6-a1b2-ae4d1ec5c028 | -8.73175 | -62.41761 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca9da13d-8f29-3944-9707-a920996a56c2 | -7.27999 | -60.65429 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bde28030-9d96-3b74-8d33-f025bca525b7 | -6.39936 | -58.2122 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 74f55737-5d8d-3a0b-8844-da5f4817310b | -11.66241 | -52.17999 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 51b7cdc0-5908-3cf9-81b1-56ebcdd6012b | -7.54156 | -63.84331 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15d3eede-c7bb-3a0a-b36d-6fe5d3f5a06a | -9.72761 | -48.98071 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 05710dfd-58c5-326a-96dc-89725ced9d0a | -8.68351 | -62.3992 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85c94a86-b308-3b7b-89bf-882336649af8 | -6.79301 | -52.81057 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f887215-bd2b-3e36-b45b-a10caf5e8b18 | -6.82961 | -52.82594 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 931f0b51-0465-3632-9b88-e36c4575015d | -6.42905 | -55.61364 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c7ec5b8-f1bf-37ce-8038-139a91011464 | -7.60417 | -61.60497 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d3e2210-4c77-349a-a38b-8b289fa1f93c | -8.66891 | -62.83706 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b95b14fe-7e04-36f2-b318-50eb2ed9a8d6 | -6.79396 | -52.8038 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20a102e2-c39a-3a0a-bf3f-6540b5e6f276 | -11.43047 | -55.18007 | 2025-09-02 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5eb2564-b629-3f7c-be8d-8b0c1398e978 | -6.89867 | -59.79465 | 2025-09-02 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a58b0a7-05dc-3635-a74d-184d396c405c | -6.82972 | -52.83202 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66d16a9a-a81d-3af1-9013-e5d34923827a | -6.85325 | -52.82193 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f742c7da-4b9e-38ec-8a2e-0288cadb5869 | -9.25445 | -60.49316 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README77.md)
