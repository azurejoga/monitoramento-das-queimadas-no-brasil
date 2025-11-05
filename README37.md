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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ace4cb8-7508-3940-9b33-0dd611074269 | -2.66644 | -54.7653 | 2025-11-05 05:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ae13c6e-ca4e-37c9-907a-c821a90cb591 | -3.44116 | -50.24496 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e42bafea-d161-382c-8998-2f87b2d0a6bb | -1.30195 | -49.15424 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 00b9135d-6ebe-312a-9a83-6e421cdffaa1 | -2.78679 | -50.3186 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4ebc6b36-efc2-3dd6-bfe4-68ddea65bc3f | -3.27496 | -53.26553 | 2025-11-05 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84f6d5c9-982b-342c-b31e-0faa67fe1855 | -3.50398 | -54.37433 | 2025-11-05 05:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b115b84-87d2-3c99-930f-9ddf31b07199 | -1.28353 | -49.14602 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3eec35d8-4fde-30ba-a15d-1ef25c9d92ba | -2.61434 | -49.22989 | 2025-11-05 05:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e7b537f-3a30-340b-93e1-c265af8038a1 | -2.79482 | -50.31233 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a959e1de-e0f5-3230-8046-2feea4854424 | -1.28993 | -49.14703 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b03a642c-589e-34a5-acc3-19c02bfc8a20 | 0.25397 | -50.95768 | 2025-11-05 05:31:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 70798811-90ec-3ed2-906a-f6e0fbd8ed76 | -2.96303 | -48.59916 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47202025-1384-3f85-96f6-51b265ec9e04 | -5.14846 | -60.37516 | 2025-11-05 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad65d32c-a060-3d3c-a14b-c3b1441096ef | -2.65077 | -48.51259 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6c65028e-8a0e-3410-a2dd-a6d6ee4c073f | -2.42441 | -49.30308 | 2025-11-05 05:31:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2a403ba-1c07-3653-ab01-a76c1cf5d5db | -3.82105 | -52.35701 | 2025-11-05 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6e2af22-fd0b-3754-a453-ad032af7b82b | -1.30835 | -49.15526 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 291d328a-0618-30f3-a5c0-742c4463f536 | -3.72264 | -54.21429 | 2025-11-05 05:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8954d594-02c2-3988-aa82-424f838cca2b | -2.62082 | -49.23092 | 2025-11-05 05:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 842e47f0-8653-3bec-8467-8268095ad5fe | -2.37739 | -53.97717 | 2025-11-05 05:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75c13edc-8280-36ef-9f8a-0d0e0b261d36 | -2.3778 | -53.97881 | 2025-11-05 05:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| daec4bba-1a07-32a8-9d51-72cfb744fb2a | -1.24327 | -49.14211 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d265d71b-0327-398f-8a93-0b848351d11e | -3.14649 | -50.29342 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbe59dd2-6dd3-31f5-863e-b8ef21a3ec1e | -3.07218 | -47.7743 | 2025-11-05 05:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| accb6690-c923-3bfd-b83c-c88f06566886 | -1.98157 | -56.5723 | 2025-11-05 05:31:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac5d2070-73a7-3292-9b25-4ae2af9ede43 | -3.49071 | -50.46011 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bddd89ce-acec-3896-8eb6-d2c5b7742d6e | -2.4187 | -49.29716 | 2025-11-05 05:31:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36b308ea-b145-3e67-a4ca-1852e3a65c90 | -3.49006 | -50.46445 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4be318e8-5ce9-3da7-9144-179c6db2e777 | -2.48497 | -55.72575 | 2025-11-05 05:31:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1883405d-47fc-39d7-93e8-188d8db1c0b6 | -3.44604 | -50.21235 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09c718d4-2186-3b34-b56c-5707a945caaa | -2.65756 | -48.51353 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 20a1ff7b-b2a3-357b-9f7b-552bef601a04 | 1.11664 | -60.51252 | 2025-11-05 05:31:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95798fd3-80ec-36fd-8a45-582be164e3f7 | -1.29555 | -49.15323 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46482e23-c224-35f6-b11e-c606546cfd92 | -1.30645 | -49.1572 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52b20fbf-5b8e-39b7-904f-dc5433a7a3d7 | -4.10443 | -48.0223 | 2025-11-05 05:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd582d6b-0d9e-3c4d-977c-c88381a17cf6 | -2.65168 | -48.50662 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1bc4b9ce-50b6-39ae-9d3a-dfe1a4ed54a9 | -2.65277 | -48.51285 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| dae94adb-e8e7-36fb-ae83-cb6f1a3a0ad8 | -4.10949 | -48.0176 | 2025-11-05 05:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c76ec61c-6225-36e0-8695-863ad606c80e | -3.82709 | -51.2217 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee483c51-aa64-3b55-9bd9-9b3765796c02 | -3.49821 | -49.55416 | 2025-11-05 05:31:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9dd22a4-e6e6-37bf-b7e2-53b90a4689bd | -1.27527 | -49.14707 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e36945ef-2313-3c16-ada8-b9b9e1006478 | -2.66467 | -54.7677 | 2025-11-05 05:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4feede7-8453-3e39-96e1-7ae41e6be1f4 | -3.43499 | -50.24409 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51c967d0-6e29-3002-b735-47b04cba5435 | -3.81696 | -51.28967 | 2025-11-05 05:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a95c852e-88a8-33a3-a173-41c2cfe150f7 | -3.84235 | -49.90716 | 2025-11-05 05:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5093426-f5ef-3980-98f3-68571fdad6de | -2.65956 | -48.51382 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77f3f5ae-e7c8-31d2-b44b-fecad5599115 | -2.98194 | -48.70595 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 050a7370-c2ff-3bb2-b984-030d84347ac9 | -5.23733 | -48.49818 | 2025-11-05 05:31:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5994685-18c7-31f3-be01-423c3988d97c | -2.42515 | -49.29813 | 2025-11-05 05:31:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbf48254-315a-3adf-8900-18a4d99b1b07 | -3.49678 | -50.46107 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c75e3449-a925-3f26-99a8-c6ab25729df4 | -1.29447 | -49.15005 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2cb5ad8d-5a99-3b40-87e4-977d9eead2df | -5.14902 | -60.37155 | 2025-11-05 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70a2addf-39ae-33fb-b54e-c2879a0c7275 | -3.24578 | -52.9196 | 2025-11-05 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afd3e5cc-700b-3613-bf55-ad9ef9a232bc | -3.14739 | -50.29184 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e5a89da-f5c3-3406-ad6d-9d12829e7922 | -3.24064 | -52.91874 | 2025-11-05 05:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb70a862-3f63-32d3-a048-3dc77da45a66 | -4.601 | -49.55616 | 2025-11-05 05:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eed6d394-142d-3df3-99c7-a3ca2fc9bd6d | -2.81644 | -54.35891 | 2025-11-05 05:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e02045a-299f-3474-8ba7-cfefd133c006 | -1.27073 | -49.144 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f452bb98-ea8f-3e8c-800e-16e87c28510d | -1.26329 | -49.13988 | 2025-11-05 05:31:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0535901-8f4c-3c4d-a046-6b79188ba22f | -3.43571 | -50.23928 | 2025-11-05 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a396c2e-fd09-3284-b05e-ec8bba1f4152 | -2.96271 | -48.59375 | 2025-11-05 05:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64b55f9d-ab8a-3aa3-ab6b-14603d418f9c | -3.14127 | -50.29092 | 2025-11-05 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80fe08f6-a4e1-340d-839d-94f11620377e | -3.07027 | -52.63062 | 2025-11-05 05:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a6b20f3-cb9a-33ec-8279-9678bb0c086a | -12.44778 | -63.15142 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5f72934-48d7-3aae-836c-4fe05c7ba576 | -12.41838 | -63.14302 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75958417-8ec0-30e0-b8cf-9fb75f69505e | -11.35177 | -55.05573 | 2025-11-05 05:33:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f21292f5-c63e-395d-a190-3157043f83b5 | -12.43779 | -63.1498 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 936b3b73-9f17-3173-bce6-25920a2b1985 | -8.05541 | -49.64135 | 2025-11-05 05:33:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d60d74a4-cdea-3998-8283-64b569bff7d4 | -10.23165 | -65.22369 | 2025-11-05 05:33:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b38c719-3961-3ef5-a111-1a72b588da7c | -12.42171 | -63.14356 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dcf9ec8-f2b7-3b35-b309-6df56d232891 | -11.79434 | -62.74938 | 2025-11-05 05:33:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ead7549b-7693-3595-a44d-ce94f08b2754 | -12.45166 | -63.14842 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 047d86e8-a5c0-3730-b812-228a1da0a4b8 | -12.42115 | -63.1471 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f12855f9-d96c-3d82-9f34-7fe15fc27f10 | -12.41893 | -63.13948 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9e62c0f-ea68-3056-aae3-f57bb5cda42f | -12.44556 | -63.1438 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b3421fe-70a4-3583-aa40-c3940de0eaee | -8.0545 | -49.64202 | 2025-11-05 05:33:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 973ea2fa-a4f3-3252-a5e7-83552958cad0 | -11.99823 | -63.94117 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0147a707-848a-36db-86b9-4f05b9d2a067 | -8.05613 | -49.63549 | 2025-11-05 05:33:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9a2621b-7220-30b3-bcb1-9bd102c2edd1 | -8.04845 | -49.63533 | 2025-11-05 05:33:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 59a4ebde-7e86-37e6-a9b4-dbf2b2238df8 | -12.86741 | -60.20536 | 2025-11-05 05:33:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71aa72d8-7191-39f6-a67f-d996fa878b4f | -8.05525 | -49.63622 | 2025-11-05 05:33:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 107566b6-60f6-3e20-92bb-2d5fae21108e | -12.44445 | -63.15088 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 635a0dcf-1f13-369c-a13f-e22573851307 | -10.92667 | -69.20738 | 2025-11-05 05:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20d51e89-9fda-3211-b101-b53123c66ce1 | -13.72405 | -51.45817 | 2025-11-05 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f6abb7a-2827-30e4-880a-e885ae331796 | -12.2525 | -62.34064 | 2025-11-05 05:33:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eab33644-9bd1-36a2-beed-7f28f645a1de | -12.42725 | -63.15173 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ef86b54-9205-3d48-9966-1ac9abdb2e79 | -12.42614 | -63.13702 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6591eb4-48f0-3bac-b1ad-9381144ff08e | -8.85778 | -49.87852 | 2025-11-05 05:33:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4a2fc98-c3d4-35d1-83ba-90dd43e4f975 | -12.42226 | -63.14002 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55e8b2c2-e5cb-3583-829d-59baf90c16c4 | -12.42781 | -63.14818 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6f69690-fbc6-3917-bc3b-f1ac60080273 | -12.44833 | -63.14788 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0d2d7ac-115c-30a4-aedf-732dac755196 | -12.42448 | -63.14764 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71324e06-e876-3c74-9a84-932c9568b563 | -12.00545 | -63.93872 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00ffa8ba-ee0d-3bca-a401-812275a7e872 | -12.445 | -63.14734 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6377388-140c-362c-b754-434e2e5524bd | -12.37866 | -64.03633 | 2025-11-05 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 869c2c75-edd1-3888-9692-507b3cb3918f | -11.89067 | -63.44893 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6331c4e1-544a-3ef4-a903-df50146735a4 | -12.43114 | -63.14872 | 2025-11-05 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a7eb700-e463-33c3-ba9c-2172adecf802 | -7.94335 | -49.73742 | 2025-11-05 05:33:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bea9d15e-89c7-365c-95ef-78e87e8687f4 | -7.93662 | -49.73634 | 2025-11-05 05:33:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3606d24a-8b91-3473-ab4e-783fd352c1fd | -8.06221 | -49.64228 | 2025-11-05 05:33:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README38.md)
