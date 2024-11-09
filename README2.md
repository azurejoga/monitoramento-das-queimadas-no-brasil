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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 004a8752-bd5b-3caa-b432-ac6bda2f8758 | -4.6268 | -46.5435 | 2024-11-09 00:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 5a619045-3594-3e86-82f6-20f96dfa0c9c | -1.5164 | -52.1696 | 2024-11-09 00:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| efaa28f5-bb14-3eec-809c-1079f6bb5761 | -2.1931 | -53.6428 | 2024-11-09 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 864fb450-c9c9-3ac7-91aa-f76d653f3447 | -23.8884 | -54.0649 | 2024-11-09 00:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 129.4 |
| 5f47669d-c589-3716-af11-91165644ded8 | -2.7945 | -49.6666 | 2024-11-09 00:10:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0c00f300-09f4-3d07-8b1c-a3748293e5fe | -23.9095 | -54.0606 | 2024-11-09 00:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 90.7 |
| 1c15ae1b-887a-35c2-bf55-1987a353301f | -3.1641 | -54.4854 | 2024-11-09 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 8e6289a9-3156-393d-9f85-2b577f60c87b | -23.8889 | -54.0426 | 2024-11-09 00:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.5 |
| 691a203f-dabc-337c-bd9b-2fc0f1a2c102 | -2.4685 | -53.6979 | 2024-11-09 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b6d8985f-ee01-3daa-9af3-ea43f3b1c670 | -3.2624 | -52.746 | 2024-11-09 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ad6d255a-effb-3299-b80b-b3c6c8f5e724 | -4.3646 | -46.8221 | 2024-11-09 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 09e6573a-b0d1-3f19-a9af-c330706ac94b | -5.5804 | -41.791 | 2024-11-09 00:10:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 5a7362b9-2ac1-3793-9c3d-e1f75adaa10a | -3.1511 | -52.9731 | 2024-11-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 365.7 |
| b938577b-4d73-3752-87c6-51af99818b8f | -4.2486 | -47.5729 | 2024-11-09 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 1d662d97-6937-39c5-8e4f-7c99c19c5153 | -4.2058 | -48.5491 | 2024-11-09 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 197.7 |
| d8895489-e6dc-39cc-b639-5c9dd0289013 | -2.5448 | -47.1137 | 2024-11-09 00:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 84727f80-135d-3f24-a95e-9e82e2a91156 | -3.2808 | -52.7251 | 2024-11-09 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 6d13b13d-c75f-39d4-a69f-27d0c2785353 | -5.4699 | -43.6603 | 2024-11-09 00:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 0d1856cb-70ce-3738-95dd-7a70c5c705d4 | -4.2033 | -45.8538 | 2024-11-09 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 336.6 |
| c97e0151-bbd2-3385-9924-1e9695f0434b | -3.1326 | -52.9939 | 2024-11-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| c9d88e13-c8b5-3e34-87a6-65216edd4956 | -3.0865 | -50.5625 | 2024-11-09 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 8929a349-0605-3b86-a101-5ad3006cc688 | -3.5649 | -43.5654 | 2024-11-09 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 09e881ae-e84e-3106-87c0-c63eab1f400f | -3.9485 | -48.1508 | 2024-11-09 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| cef82435-4e8d-36b1-a572-823cad62545e | -1.1467 | -53.6573 | 2024-11-09 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 52fc6563-6f27-3273-b0b0-b75fed0c666b | -3.0947 | -53.3196 | 2024-11-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 13458652-ec57-3f36-84af-beda9792f8fa | -3.068 | -50.5631 | 2024-11-09 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e54cc6b9-6a63-3193-8424-fb26de7c0c8d | -4.2243 | -48.5482 | 2024-11-09 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e72e9f6a-d776-3bd5-b51c-77792deefea2 | -3.1512 | -52.9527 | 2024-11-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 8989d3fb-defb-3116-ab14-4607cca7d5bd | -3.9669 | -48.1716 | 2024-11-09 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 230.0 |
| 344de721-a84a-33cc-bedc-ae92506eccd7 | -4.2486 | -47.5729 | 2024-11-09 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| e7bc4458-ad98-36df-83c0-7d635e99b325 | -4.346 | -46.8231 | 2024-11-09 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.4 |
| c7b017a8-1b26-353b-85bc-4347b756a234 | -3.2353 | -50.2645 | 2024-11-09 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a2fbb970-10e2-3a3c-827b-bae9eac6ddd5 | -3.967 | -48.15 | 2024-11-09 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 6dbb5d3f-f6f3-327c-9174-54fe320eee83 | -4.2236 | -48.6772 | 2024-11-09 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| aa769b9e-c044-32fd-aca0-9796aa1acd47 | -0.2115 | -51.6249 | 2024-11-09 00:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 7d73995e-217b-3e91-816c-5b52bc0d1d5a | -3.151 | -52.9934 | 2024-11-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| bd9bd163-132c-3658-bb03-9f203135a94e | -1.5078 | -47.1813 | 2024-11-09 00:20:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 512e24cb-462b-315b-9df6-854038ed126c | -5.4701 | -43.6371 | 2024-11-09 00:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c701f72d-8add-3f0b-85a7-972c5648218f | -2.5748 | -49.1208 | 2024-11-09 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 72eea3b0-6843-35b8-89f2-fa454902c414 | -3.9668 | -48.1932 | 2024-11-09 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| b4f7df7e-0274-3b8e-ac81-7f630c564820 | -1.5164 | -52.1696 | 2024-11-09 00:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3db6b262-764d-31b9-aa97-cf2b9d899b9f | -4.2219 | -45.8529 | 2024-11-09 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ee51058c-a6d3-39e0-952e-1073442f1bdf | -4.2032 | -45.8762 | 2024-11-09 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 172.0 |
| 7e5f0ea2-c85c-3e80-bab9-362e810528a3 | -3.5462 | -43.5663 | 2024-11-09 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 2fa2a063-b2b3-36d3-8616-a8c026f68030 | -3.2624 | -52.746 | 2024-11-09 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| a7b4cb1e-3e38-3911-af90-2294a7a9fab2 | -2.5747 | -49.1421 | 2024-11-09 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7b39e7ec-375c-36a9-bc5e-9475d99b4724 | -2.4104 | -48.5265 | 2024-11-09 00:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5b1ddaa2-670b-3f1c-b3da-2b4f66204d17 | -3.1511 | -52.9731 | 2024-11-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 495.7 |
| beeaed7c-d61a-30ec-8bc7-d2fe44b29b14 | -3.2808 | -52.7455 | 2024-11-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| d66a881f-5409-3262-b396-b0fa79b34467 | -4.3646 | -46.8221 | 2024-11-09 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 9e72450f-0a57-38bb-a031-366f8ac994ab | -3.1327 | -52.9736 | 2024-11-09 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 2cc24147-66ca-3162-8b86-c568eb6239fd | -3.0321 | -50.3128 | 2024-11-09 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| aa544fb1-1878-34be-9e59-b2c04c3c665a | -4.2484 | -47.5947 | 2024-11-09 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0d573305-ddff-35fc-84bd-5184ecf75079 | -4.2671 | -47.572 | 2024-11-09 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 0696557b-ec22-3711-b2d0-c8f198f845c5 | -3.9854 | -48.1708 | 2024-11-09 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 130fc739-60ea-34c5-a8bf-13f7d875b49b | -23.9095 | -54.0606 | 2024-11-09 00:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 101.6 |
| e4d46d57-a80b-3c02-9454-4a83150ee8ae | -2.2295 | -53.7832 | 2024-11-09 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c0226060-0d0d-38e1-9b10-ab87d5a38ef9 | -3.735 | -54.2292 | 2024-11-09 00:20:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a2e187f3-8e2b-3cff-b618-9372d043b8c2 | -4.1872 | -48.5499 | 2024-11-09 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5b131eaa-6710-3344-b035-b8d59c19ca55 | -2.6764 | -51.8189 | 2024-11-09 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 5ba9aea8-5599-3149-8ed9-b8370e8aaa3b | -2.2295 | -53.7631 | 2024-11-09 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| e6162c03-50ac-3c6c-b764-761ec5ff89e1 | -4.2059 | -48.5275 | 2024-11-09 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 53f5c76d-f985-3f42-b14e-9922b69c5233 | -4.6268 | -46.5435 | 2024-11-09 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 0ba54d67-364f-3ffe-82c5-8167f582438e | -4.2487 | -47.5511 | 2024-11-09 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9d06540d-9816-312c-a69d-b08345e81706 | -23.8889 | -54.0426 | 2024-11-09 00:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 88.7 |
| 6fed652f-606c-3743-9a04-f5a12580d494 | -3.9483 | -48.1724 | 2024-11-09 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2cd1cf23-e60d-3285-a291-c12841451b7c | -6.9937 | -40.0277 | 2024-11-09 00:20:00 | GOES-16 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 135.4 |
| bf20edd5-4767-323c-b543-40bce591cd05 | -2.4365 | -46.3019 | 2024-11-09 00:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3cecc05a-c14c-3ee2-be30-93a1fe6bf673 | -23.8884 | -54.0649 | 2024-11-09 00:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 146.9 |
| ca7c53b6-dad3-3e2f-950c-4673aa7b5c1f | -3.1641 | -54.4854 | 2024-11-09 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e49fc286-b442-348f-94b4-dbb47a155152 | -6.9937 | -40.0277 | 2024-11-09 00:30:00 | GOES-16 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 158.4 |
| cdef354e-b3cf-3236-8c09-17f12219ef2c | -2.2295 | -53.7631 | 2024-11-09 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 10abf9a0-40d2-39bd-918a-69765b0cde6a | -3.0321 | -50.3128 | 2024-11-09 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 3351d521-1e7d-316b-ba59-f306ecd548c4 | -3.5461 | -43.5894 | 2024-11-09 00:30:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 040b2741-727b-38ee-80c0-6cdad70dcf8a | -3.2808 | -52.7455 | 2024-11-09 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 692773cb-5778-3edb-bfeb-7f753d1c5d05 | -4.2033 | -45.8538 | 2024-11-09 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 298.1 |
| 039407f6-3bfe-30f3-bb1c-f56d4b4ae93c | -3.0947 | -53.3196 | 2024-11-09 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d787bd24-04be-3b7c-8119-173d57131bbc | -3.2624 | -52.746 | 2024-11-09 00:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 862f297c-6d8c-303d-864b-8f68c73670b7 | -3.2353 | -50.2645 | 2024-11-09 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3d4ea3c3-9445-34f6-b037-963e59d4e4dc | -4.23 | -47.5738 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d9dc6bd2-a23d-3294-83f2-5c5f51217c93 | -2.5448 | -47.1356 | 2024-11-09 00:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ae53e6e1-74ef-337a-b3c2-e1bc0fd308f9 | -7.235 | -38.8977 | 2024-11-09 00:30:00 | GOES-16 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 5abf0bcd-88bc-31b3-b5aa-4bc20e469152 | -3.5462 | -43.5663 | 2024-11-09 00:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| c6fd0df8-242f-338f-b72c-5ab69636da63 | -7.2346 | -38.9231 | 2024-11-09 00:30:00 | GOES-16 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 238.7 |
| 30a70354-4d4f-380d-8f0a-d655a257cafb | -3.0865 | -50.5625 | 2024-11-09 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 313c8abd-d5a7-3213-8536-efc84b026553 | -2.5747 | -49.1421 | 2024-11-09 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a5f46da3-fd92-3e16-828d-f14483425344 | -4.2058 | -48.5491 | 2024-11-09 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 212.0 |
| b6c4c498-29e0-3e22-b87f-157e28dd95c5 | -2.5448 | -47.1137 | 2024-11-09 00:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| f0738b6e-5d83-3fd9-be46-f708ac185967 | -3.9483 | -48.1724 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| fa2867d1-a635-3764-949a-17f593cf8602 | -7.2343 | -38.9485 | 2024-11-09 00:30:00 | GOES-16 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 4fd1657d-f5ed-3d18-adde-9f7a992c3142 | -3.9669 | -48.1716 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 256.9 |
| 81ec8588-121e-388f-8df4-e1f33fa6e516 | -3.1505 | -44.4111 | 2024-11-09 00:30:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 2fe9cdcb-64eb-3442-bca0-199300717d2e | -3.9485 | -48.1508 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 26ade9d0-6de0-34ee-96c2-faa97147d468 | -3.1319 | -44.4119 | 2024-11-09 00:30:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 515e5f9d-f3e8-3aaa-a4c5-92d01c58bde5 | -6.9934 | -40.0525 | 2024-11-09 00:30:00 | GOES-16 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 75ef8afd-577b-319d-b767-8ace1ea0cd40 | -23.8884 | -54.0649 | 2024-11-09 00:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| a4d351b0-f4ad-33ab-8a6a-b47d86a059ed | -4.2059 | -48.5275 | 2024-11-09 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 97479503-e7e0-38c0-8c10-31a2d7cdf071 | -4.2487 | -47.5511 | 2024-11-09 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| bb399f86-7b2f-399a-b52f-96fa0b254dd5 | -2.6764 | -51.8189 | 2024-11-09 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2fe7ab05-8245-36ef-88ff-b1314dae3c37 | -5.4699 | -43.6603 | 2024-11-09 00:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 190.2 |


[Clique aqui para ver as próximas entradas](README3.md)
