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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2a9b628-53c1-3101-8fb4-4df3e9ac174a | -8.48351 | -46.85403 | 2024-10-02 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c093dfe0-c3fd-34b9-b57f-992f0a73103a | -8.48282 | -46.85725 | 2024-10-02 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5e528ed-a388-3233-b436-9807b0d34db9 | -8.47959 | -46.85206 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0081f9bc-c25e-39a5-a77d-fb841ae5114b | -8.47958 | -46.85356 | 2024-10-02 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0ba7b07-f227-3ad5-b00b-dc4d8399577d | -8.47892 | -46.85824 | 2024-10-02 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c233d50b-2887-3667-a0e4-9b2c1ea46d73 | -8.47889 | -46.85679 | 2024-10-02 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e84ab436-1b97-330c-9e26-e9073e8a70c1 | -8.42835 | -46.44915 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 907ff2be-6bc7-3af0-8ab4-dcf130a844a0 | -8.42658 | -46.44978 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a56c4d5c-9ba8-3f04-b6f0-b3a62160949c | -8.41611 | -46.32423 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e044df3f-0c24-31dc-9d5a-c20d8f868a26 | -8.38658 | -46.38593 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6abef83-6d8c-30c2-b0d3-6c4887fbd2f0 | -8.38359 | -46.37812 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e91cc6a9-84dc-30a7-a1c5-d2a504d849d5 | -8.38307 | -46.38175 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f6dc0b4-0d3a-3822-b8e6-d8bd4a150b3e | -8.03396 | -46.0618 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3016cd56-c0d5-3ad5-add5-327c9a9f7c76 | -8.02388 | -46.04484 | 2024-10-02 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 973f236d-1384-32cb-bfd7-5c3c0a04e2f4 | -9.76772 | -46.06562 | 2024-10-02 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c5cc90e-bf70-3656-91be-3b763f47ed09 | -9.76353 | -46.06495 | 2024-10-02 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d948298b-6d23-305b-abf8-1d367b3f5d5c | -10.70031 | -46.16346 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60ddc99c-8236-3a4c-b848-22cc8ec5a10a | -10.69663 | -46.1589 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2116652-2483-3d5a-ba2d-47f42f4df403 | -10.69606 | -46.16302 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b299af64-06e7-3aed-af96-43957939a5fd | -10.69296 | -46.15428 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 670f7acc-085b-3d3e-9d60-22a9986c0501 | -10.69239 | -46.15839 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9d96508-aa80-3f7e-a3ea-750c8602b05c | -10.68928 | -46.14963 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb622cbc-1d5d-3541-ad87-71390def77ea | -10.68871 | -46.15377 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3bc5188-8f63-3ffc-8667-f5457c1c10a7 | -10.68193 | -46.14034 | 2024-10-02 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ac5ed9d-529a-389c-b8e2-dc8091814b33 | -10.5069 | -46.03291 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98abc9dd-bbb1-3349-816c-0d6736ce1aa7 | -10.36627 | -46.14299 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4af605b-f502-3a92-8e5f-04b682f3e128 | -10.36205 | -46.14241 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f9d675d-eb0c-3454-9a81-8245c13952fe | -10.3211 | -47.45657 | 2024-10-02 04:46:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 21115f5f-75fc-3b02-b788-9fc32367e435 | -10.08385 | -46.8497 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd521877-6a19-39c5-8f06-a3120b446232 | -10.08284 | -46.85668 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5bfa5f91-64c0-3163-bbda-16135ffbe6ca | -10.08235 | -46.86015 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 40442f20-fbcb-3b5e-818b-e84ebd303547 | -10.90942 | -46.33567 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba90528a-16cb-30d8-a21d-84361b64617b | -10.90888 | -46.3395 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d4af19a-8344-3c2c-9415-4cbdc593d42d | -10.90524 | -46.33493 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dfec85d-aa5e-368f-8af2-84d6b4dc52f6 | -10.90106 | -46.3343 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55697196-21c9-3c0c-a3bc-8d38effe0017 | -10.88014 | -46.33103 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84d2b8c5-ef8c-337e-a1d8-32fd0bdfafb5 | -10.51225 | -46.30959 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 105dd572-e21c-3951-810f-847920f9e404 | -10.51172 | -46.31343 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 190aef49-d2ed-390c-85b3-398c9950ce56 | -10.50808 | -46.30891 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3dd09fa-acda-3cca-93b4-6f44d3d8bc53 | -10.50443 | -46.30442 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7de509d4-fd35-3fa4-beef-63929e5cee7f | -10.50289 | -46.30552 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 409d4780-352b-39ee-8a0f-1ac870f7402c | -10.49926 | -46.30106 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d34874a9-17d7-3575-aadc-41fc809c2881 | -10.4966 | -46.29932 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35fa6559-6ce2-3271-8f1c-1c285a4d004d | -10.49564 | -46.2966 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8767e4f9-d411-31d8-8ea6-543a77f0a87d | -10.49145 | -46.29603 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 290d8c54-3cfe-3193-b64c-8390a29c3f5c | -11.01523 | -46.5178 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 62f38bf2-aa23-3b91-aeed-5cf65d61f5b4 | -11.015 | -46.48814 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65c01f0a-cdd0-3c46-8d02-dea2350b67ea | -11.01343 | -46.51417 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fc157378-db25-3285-bd14-6ce9cd3a4727 | -11.01289 | -46.51795 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 91e9415d-faea-3d57-86e0-8b53836b72a3 | -11.01288 | -46.48816 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0815461a-f01b-3d57-bd26-1edd2878f8a0 | -11.01108 | -46.51718 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a1fce72-4e39-3707-8d8d-e16d8a4b71f1 | -10.99707 | -46.56998 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 56ed74ba-bfbf-385a-9ee8-76d7b26559d5 | -10.9963 | -46.45522 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df08b719-803d-3077-ab8f-8db42be4dbe6 | -10.99322 | -46.4469 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 105e4cf8-44fb-323e-969c-ec2d79473956 | -10.99294 | -46.56942 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ddceb0a3-5469-3a47-9d2c-2696a652f697 | -10.99269 | -46.45069 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c032070-82ff-3d9b-962f-8db214638442 | -10.9924 | -46.57323 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 08674e51-3369-3b63-90a0-dd022dd3f753 | -10.98573 | -46.5607 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e5cd5da-66ac-36ba-98f7-ad70e524ee4a | -10.91883 | -46.36823 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1ff4bbe-2671-3f45-bc29-bc97e296e7ff | -10.91769 | -46.3377 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d9aba80-8a2b-37bf-aaa8-ad36771c3a50 | -10.91751 | -46.36922 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61d74ae7-462a-361b-aa38-b12ca7f7734c | -10.91662 | -46.34529 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41fa2717-030b-3e07-8e52-80010014fd81 | -10.91443 | -46.36084 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4b8ffc6-296e-32be-8776-572d2c49f55f | -10.9139 | -46.36459 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5183a67-5b6b-3abc-bcd2-354a60d8dacb | -10.91339 | -46.36821 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1de1293c-28bd-3fed-970f-f191df6ecf42 | -10.91304 | -46.34031 | 2024-10-02 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd984b95-26e2-3889-923e-1c2a6a8b4123 | -11.96512 | -47.3685 | 2024-10-02 04:46:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19a84b42-0bb5-300b-971d-c414f56a0b2e | -11.96438 | -47.37372 | 2024-10-02 04:46:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a9d4312-3191-383c-b56b-6ff69780db2d | -11.86777 | -47.11829 | 2024-10-02 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7853c4fc-481b-37e2-ae57-a10deb5f3142 | -11.82995 | -47.30134 | 2024-10-02 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e78218a9-dc37-3541-83ec-36b316776a43 | -11.82596 | -47.30076 | 2024-10-02 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 334afe37-0aae-3276-9ccc-c7e9696dcdc0 | -11.76224 | -47.61399 | 2024-10-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4effb2b2-0d21-3f3b-b702-59f542503630 | -11.75833 | -47.61345 | 2024-10-02 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c17486d3-5703-3b09-ab69-5389b8339ed0 | -11.29965 | -46.83964 | 2024-10-02 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3afd6c7-5195-3027-ba89-1466b6f0c4be | -10.94643 | -47.28926 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af741aea-99ce-3b86-a030-4c51a29306a1 | -10.94393 | -47.27832 | 2024-10-02 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2349ee19-7005-30d1-a239-d45b3944f1bf | -4.92119 | -47.44747 | 2024-10-02 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d219b43c-89c1-3652-81f2-b3f786ab3539 | -4.92057 | -47.45161 | 2024-10-02 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4908b66c-1ce6-39e6-894d-30647a39898f | -4.91974 | -47.44826 | 2024-10-02 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3747b178-6113-343a-8d9f-9dc3de1158e7 | -4.9191 | -47.4524 | 2024-10-02 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42acfd12-407d-3f08-a180-be4ad2a1427c | -4.87429 | -47.40685 | 2024-10-02 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6419091-eab9-3f5e-8548-00b12ce3e2d8 | -5.38705 | -47.70309 | 2024-10-02 04:46:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20c27af3-8f55-3e0c-9398-9ce49fa8d332 | -6.28243 | -46.99086 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da2a0d19-8fec-3241-a6b3-229f33827d0b | -6.28176 | -46.99545 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9495ff2c-88ae-3a4f-8507-dc5223eaf4f8 | -6.28171 | -46.99263 | 2024-10-02 04:46:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1edbbc69-ad73-379a-9bb5-f2c4173dd6ad | -6.12331 | -47.26992 | 2024-10-02 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 11a68044-3285-3129-9b63-7cb0576a8b71 | -6.12264 | -47.27433 | 2024-10-02 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 113cad6d-b96e-3cad-86e5-04d5b1ac8aa2 | -6.11961 | -47.26936 | 2024-10-02 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efd99afb-4586-3c88-aa88-1f6a3668dc96 | -6.11894 | -47.27377 | 2024-10-02 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0dc04def-c155-314c-8717-95f62dcbcc43 | -5.73358 | -47.10194 | 2024-10-02 04:46:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 370e7fee-2683-3dd8-a71c-513de0295906 | -5.73229 | -47.09929 | 2024-10-02 04:46:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52e65f40-cf8f-374f-89c1-3177508db326 | -5.24187 | -46.77252 | 2024-10-02 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60f12fd0-d050-3f4b-b27f-5e0bb8a4a2f9 | -5.2416 | -46.77038 | 2024-10-02 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 035fbcfc-7953-376b-9893-046051ec5a50 | -7.48948 | -48.16557 | 2024-10-02 04:46:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a4a90b9-f1b0-3d13-b7a6-d4f636fda745 | -7.20767 | -47.69942 | 2024-10-02 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5a6928f-e8cb-3d0c-902e-0f1163ed603c | -7.20401 | -47.69887 | 2024-10-02 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67c1801e-c659-3ffb-a52a-f6ee72003ebb | -7.10709 | -47.86982 | 2024-10-02 04:46:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8ed51e5-c254-3e0c-b266-3bca3fba5b80 | -7.10348 | -47.86916 | 2024-10-02 04:46:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bce4a05c-f345-32c4-9842-0a01a84d1653 | -7.09986 | -47.86855 | 2024-10-02 04:46:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a7e59ae-20bb-3707-bf4c-d0231b2a25fb | -7.09923 | -47.87273 | 2024-10-02 04:46:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README88.md)
