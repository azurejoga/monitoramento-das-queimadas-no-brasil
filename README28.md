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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 517877b6-ede2-3c79-937d-a260c4ebe36a | -2.93133 | -48.067 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b0aa7b9-19f5-3746-89f5-93e34b122293 | -2.16393 | -48.9137 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 196b3be2-37f1-304e-b38e-33044f399a8a | -2.66642 | -46.84696 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5778850-2fd6-3307-8445-c2dfb9551534 | -3.28011 | -45.50571 | 2024-11-16 04:23:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 08175ed1-dbd4-39af-afbe-01c59365560b | -2.07482 | -46.47845 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46da1c31-d04b-35cd-8bb2-ba9c5089abee | -2.65682 | -46.17519 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf73612e-f16e-30d2-b830-8e25458a1e2e | -3.19882 | -45.54896 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 20aefaa0-503c-3df9-a5d0-2ed748cf702a | -2.13113 | -48.77843 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29359bb7-aee1-384e-b71d-f4f58b241bda | -4.35952 | -45.76688 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fa0a602-e761-33cb-bfe3-2478589a33d7 | -3.7657 | -43.25059 | 2024-11-16 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb5cd03a-0cb2-36b8-809f-84d7266afb13 | -2.82183 | -46.66429 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf0409a3-e575-3b94-a465-401a1bac5e88 | -3.75842 | -50.79662 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 011768f8-d97d-3123-a92f-6b806bd8c1ad | -4.35681 | -45.86533 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aadb1629-7bbe-3264-b6a6-2d729a970ba0 | -3.58086 | -50.53229 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 82f1b9bb-739d-325c-a56e-e30bbee65294 | -4.35736 | -45.86188 | 2024-11-16 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb219fd3-667c-3892-902b-b0c7b8ae127d | -2.307 | -48.4659 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05d55d43-ecef-3cb1-8fe9-f0231ffbb2cc | -2.66351 | -46.17624 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e1a5eaf-f525-3305-8e3a-2abdd67ae7bc | -3.94339 | -46.70463 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96814c8a-f057-3210-ad6b-8062b8b3e979 | -5.66437 | -35.65091 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2bb3a081-8492-3bf2-b1a3-c6aa55893407 | -3.93078 | -42.40954 | 2024-11-16 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6a1c3ece-c9d0-3be2-a0c6-e6d5c9168e3c | -2.1426 | -46.40544 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee05b593-318b-316d-833e-43fd4dfb88da | -2.14175 | -48.73522 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 58f83b04-17a7-34df-811c-cd40e6391f96 | -2.08422 | -50.49477 | 2024-11-16 04:23:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4021087d-83a0-39f2-b8d4-1c8a533a9780 | -3.19441 | -45.55534 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 12010650-0efb-3d43-ae6d-83dad9cb0e1a | -3.10358 | -45.98042 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d831f51-607c-3c9d-b210-455cc6da217c | -3.54509 | -51.58943 | 2024-11-16 04:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16fff3e3-1d17-3cba-9cd4-796c8ad32872 | -3.57114 | -45.67434 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4971700-b427-34d5-b46f-99a62baf1c5d | -3.1008 | -45.97644 | 2024-11-16 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11fd28b6-955a-380f-b8b7-54019ff16051 | -1.23412 | -53.70554 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c79dc0b7-4b65-3701-9327-d42ba00e52e8 | -2.71364 | -46.06956 | 2024-11-16 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27a5a7a1-a368-38ec-9184-599ab2c28b92 | -1.64316 | -50.44847 | 2024-11-16 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4be8b351-9dc7-3662-80c4-b5e6b33dae72 | -4.54122 | -45.46958 | 2024-11-16 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48686411-bf0b-3eef-9c0f-6ec6568fa540 | -2.6624 | -46.18324 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2abc3e6-c7cd-3f8b-b79a-3fd6304c03ed | -2.88153 | -40.39233 | 2024-11-16 04:23:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0cad6d93-80f2-3228-89e2-31739e7828db | -4.32039 | -43.62996 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc4820f2-2690-34da-b9ed-b70a80c87a5c | -4.42136 | -45.80111 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dec10351-4134-3e83-b4ba-308c32728c9a | -2.17806 | -47.95048 | 2024-11-16 04:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2de3c9c5-c703-3296-a64c-86a3690412da | -2.64721 | -46.8365 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 633997ef-51e7-32ac-958f-44b0549ca209 | -2.3196 | -49.19371 | 2024-11-16 04:23:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb08351f-cf98-3728-a703-d33346c8d761 | -2.53205 | -46.21628 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee0bb77a-d2a4-3466-bd2c-828fc7743e4a | -4.73144 | -48.1157 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c57a0a8b-7fd4-3a5f-a6f6-53c6a6cf087b | -4.0335 | -44.10615 | 2024-11-16 04:23:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a346930-631c-32e4-8f59-f8e26eb18b6f | -2.66078 | -46.83864 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ec9fa2f-b755-3582-becf-1078da11d3dd | -2.65235 | -46.16014 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a44fe9d6-8112-3c3e-9653-864d7173bb67 | -2.3569 | -47.14756 | 2024-11-16 04:23:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f76c17ba-f7a9-325e-9d26-da58e5dafe73 | -2.22839 | -46.8348 | 2024-11-16 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d275a1b3-55c2-395b-92c6-aedb1628968d | -2.02937 | -46.37286 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4646b8b-5e0e-31ea-8d51-9057e3b0811f | -4.37655 | -48.57075 | 2024-11-16 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d1757ae-6f85-3848-8770-7c4913a1f191 | -2.64287 | -46.15508 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9e4b70c-c3f2-3e83-a3d5-39d90c3144ba | -2.06076 | -46.54587 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3600a4e5-1e61-3f33-a946-177705aec95c | -4.22645 | -50.67333 | 2024-11-16 04:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee2c6d9e-0e77-3ac2-b7d9-4a4a85f9a103 | -2.81776 | -46.66016 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51da5f9e-4586-31a5-9ac6-bb9456847c7b | -2.9093 | -46.85795 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6aeba8a3-8894-3a8b-b72a-54164dcec34a | -4.45427 | -45.7001 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12ecf12a-ab2b-3668-b80f-5892a2e416b2 | -3.78615 | -46.67597 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88be04aa-55e5-38b7-9dc6-6d8fd6fe1ae6 | -2.22935 | -53.61372 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| c33ea099-c488-3ca9-8858-a717f2a6c386 | -3.91512 | -46.52263 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f415622b-88ac-312f-a21a-18407649dad3 | -2.90988 | -46.85434 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68d05390-92a3-3003-873a-820bdb2b5cb8 | -3.11061 | -45.89268 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6be8e5d7-a161-3072-be75-a2d2420306e9 | -2.90369 | -46.84963 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70ae756a-d922-3a2f-90c3-8f9dc78f2bd8 | -4.37544 | -45.79039 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fd97c59-e5ee-3d55-b4fb-c0fefe7949f1 | -4.40698 | -40.69423 | 2024-11-16 04:23:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3336643f-03f3-3f69-84b8-960eceb52351 | -3.50487 | -42.00507 | 2024-11-16 04:23:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f9f2a9e6-8c39-33e0-ae6c-448fe9be9265 | -2.6602 | -46.19726 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c96ab1d8-d4a7-3ec4-940d-c70d61390463 | -2.66756 | -46.83971 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cecd79f8-6a25-3f46-8618-ec1b68d6be99 | -3.85842 | -51.81617 | 2024-11-16 04:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3df05db8-9c0f-3f81-b892-345cf91a12bc | -3.01561 | -47.97093 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89cd1b59-cfbd-3b92-aa9c-d0d270b39a87 | -4.9159 | -44.78537 | 2024-11-16 04:23:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b178aac-1e1b-33e8-bf1d-c3a1eab43d40 | -2.08059 | -48.95242 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13cb67b3-661f-3383-a5a6-3e68371b5631 | -2.28896 | -46.45017 | 2024-11-16 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f0799d5-8f47-3e2f-a83b-769edbc1a019 | -3.20214 | -45.54947 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| d07707e7-dd6d-30e2-8b98-8b0f9e6ee09f | -2.9003 | -46.8491 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1139e34-1ad6-3681-9435-1cb47bb69204 | -3.12025 | -45.74533 | 2024-11-16 04:23:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13f22a64-2a83-3267-a585-5e6816862c9b | -2.22885 | -48.37184 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0705774-c12c-31d2-9a7e-65c5fbfa9e13 | -3.99749 | -46.40685 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 790af966-3e5e-3baa-b4a5-079fac933b8d | -2.15441 | -50.70515 | 2024-11-16 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a219b2ac-83e3-31a2-aed5-7588afa7f23d | -3.73818 | -45.66566 | 2024-11-16 04:23:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15af3766-ed50-30e6-83ce-988d7bfcf8c9 | -4.1911 | -40.47628 | 2024-11-16 04:23:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 95fa5fa0-89f9-3f51-8be5-49d7d42d76a9 | -4.37572 | -45.62082 | 2024-11-16 04:23:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c0d36b2-0841-333c-8343-cd47761c5106 | -4.90374 | -44.03275 | 2024-11-16 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57b55501-237d-3ce0-a040-4a780710ed28 | -2.35183 | -49.11447 | 2024-11-16 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1521cf1c-9f31-3c6b-9e7d-4eef817f399a | -5.66647 | -35.64112 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 56fe24bd-bfc9-3de2-ba44-1711dc8f7483 | -3.23591 | -45.37815 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14afec63-ddc8-3f18-91d8-a506d283dc98 | -3.94185 | -46.41241 | 2024-11-16 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8badd706-1d45-3c8b-aee4-7ce7c58ec794 | -2.64439 | -46.83231 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 848debbb-228b-35ca-9839-a32f5169b573 | -3.58433 | -50.53656 | 2024-11-16 04:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 192430a0-da20-36f5-bb3a-483bd1604b77 | -2.349 | -47.46602 | 2024-11-16 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 545cdffd-ae8b-37e0-b4c5-5f1bb12fca79 | -2.65796 | -46.18972 | 2024-11-16 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 824b9c9b-2bf4-3413-bce6-26cbfdbc5110 | -2.10976 | -48.27426 | 2024-11-16 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e369f59e-3273-3316-8966-bd8c2b7c894d | -3.0699 | -48.01491 | 2024-11-16 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc534e36-3653-3699-93e8-7229fa9584b6 | -2.64745 | -48.48351 | 2024-11-16 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 790e9eae-eec1-3967-a2b9-c2a063783a93 | -2.22887 | -53.61671 | 2024-11-16 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 662ea31e-a18f-34e7-ba2c-c699a62d2300 | -2.67775 | -46.8413 | 2024-11-16 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dccfa4b9-a23e-3510-baa2-d9eeadddff87 | -3.24494 | -45.38369 | 2024-11-16 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 787ceaa6-8c0a-3b24-ab71-3f24d778e466 | -5.67707 | -35.64465 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 5e76a4eb-76c6-300f-a00e-03a0ab4bcab2 | -2.65685 | -46.19672 | 2024-11-16 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1265416-464a-3091-a992-a7136d3b5c59 | -3.98582 | -43.71771 | 2024-11-16 04:23:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07e0f5a1-64fb-3630-81ba-8d1fde19f098 | -2.78679 | -45.95263 | 2024-11-16 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92399926-c553-32f8-803d-52e29f75ee4b | -5.66546 | -35.6429 | 2024-11-16 04:23:00 | NPP-375D | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 47eef423-ad94-3d65-ad6f-deadbdb3a5ed | -3.08529 | -45.60559 | 2024-11-16 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README29.md)
