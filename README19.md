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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7f55bea-140f-3744-95ee-9bc253c3a6c4 | -2.6595 | -46.2065 | 2024-11-17 02:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| bc632d7e-6987-3fcc-9568-ebab38ca7909 | -2.678 | -46.2059 | 2024-11-17 02:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2d15d76c-926d-3cb1-b299-3f1c81690ae0 | -1.8981 | -46.5808 | 2024-11-17 02:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 5e40df98-4472-317e-996b-9b1d279d0939 | -8.4333 | -44.2251 | 2024-11-17 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 541927f9-660b-3c22-bec0-d5f8a34f3cc9 | -3.5125 | -50.2343 | 2024-11-17 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 730264c7-1cf0-36fd-beac-d5421fe14a5f | -3.5494 | -50.254 | 2024-11-17 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 520df375-0641-3787-b1bc-7cc0822eb434 | -3.3175 | -52.7648 | 2024-11-17 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e660bbaa-1131-3198-923c-81de83511928 | -8.4522 | -44.223 | 2024-11-17 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| fe530bc5-1e71-3048-88a3-203ccaa71347 | -8.4336 | -44.2019 | 2024-11-17 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 273.9 |
| a2fe2850-9cfd-39b9-9b8c-b6ed7009ccfc | -2.2296 | -47.2316 | 2024-11-17 02:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 3371486a-421a-3a92-8d31-7a99a213e56f | -4.5614 | -48.0141 | 2024-11-17 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| b018af61-e09b-3b2a-8a77-1f3ab6ec9168 | -2.2111 | -47.2321 | 2024-11-17 02:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 53595eea-f11b-3817-a22a-06cfb699be77 | -8.4339 | -44.1788 | 2024-11-17 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 8853ae12-26a8-3f43-ace1-211a11bc278e | -3.5851 | -50.5255 | 2024-11-17 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 22ae105f-c0be-321b-bfa9-7f734c065859 | -3.3359 | -52.7643 | 2024-11-17 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 1cc95586-28f9-3289-8c9d-128ec9182ba9 | -2.8614 | -46.7306 | 2024-11-17 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 9d141944-0888-3678-b78a-5e67ec63b2dc | -2.2296 | -47.2098 | 2024-11-17 02:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| 77d4b65f-c5d7-38a1-8858-6e2394cffa38 | -4.5616 | -47.9925 | 2024-11-17 02:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 2864a6c8-d04c-39d1-aede-ef23dd673793 | -3.3359 | -52.7847 | 2024-11-17 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 3ddc0986-b5c3-38b1-8cc9-e27ea8b34a2c | 0.6159 | -51.7676 | 2024-11-17 02:30:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 8d06d9ca-4057-367a-952c-0aa6e8580380 | -8.4525 | -44.1999 | 2024-11-17 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 291.3 |
| 5fb15aec-03df-3248-a2b3-4b70251730af | -1.5073 | -47.3996 | 2024-11-17 02:30:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 4b8bccb6-666b-3112-8a0b-4d066c305ce3 | -1.9167 | -46.5584 | 2024-11-17 02:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 2abddbf9-70dd-3d4b-a1c5-cf1bba3a3e1b | -2.8615 | -46.7086 | 2024-11-17 02:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 94267265-059f-32d7-8ca2-953d87a7b4fe | -2.2111 | -47.2102 | 2024-11-17 02:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| c58c9514-8eb5-3105-bdc9-e5f952e9247f | -8.4528 | -44.1767 | 2024-11-17 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 6b2d4a35-9114-3cb1-8759-8a7742210156 | -2.5802 | -47.571 | 2024-11-17 02:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| cdd815f9-2802-3f4a-b91a-cc4be4fa4d44 | -2.5987 | -47.5705 | 2024-11-17 02:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| ee04c18e-8023-3788-95ba-33a0781f6695 | -3.5124 | -50.2553 | 2024-11-17 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 986e48a2-de80-3783-b998-2f03877c9199 | -3.5308 | -50.2757 | 2024-11-17 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0dfcd13e-62a7-3d10-8d83-a370eb34a753 | -1.4888 | -47.3999 | 2024-11-17 02:30:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 5cc75e41-1d52-3e1a-a95b-d3012216b2f0 | -3.531 | -50.2337 | 2024-11-17 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| fae6c045-030c-3e22-85f4-128874ac582a | -3.5309 | -50.2547 | 2024-11-17 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 301.9 |
| bd7f495f-b535-3315-8a38-a947fb5600ec | -1.4888 | -47.3781 | 2024-11-17 02:30:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b958507d-b287-36a3-aff1-96f63aa1b9d2 | -2.5988 | -47.5488 | 2024-11-17 02:30:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| b77b50ac-e36d-3d6f-840e-1b534b13d531 | -1.9166 | -46.5804 | 2024-11-17 02:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 19895d81-6cd0-36d6-a760-4b8d0cdec3ad | -2.6322 | -48.5634 | 2024-11-17 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 0131a816-f846-3d51-92e6-5b67ae49dd2b | -2.2296 | -47.2098 | 2024-11-17 02:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 7f055bcf-df59-37b9-b406-8c865299c33e | -2.8614 | -46.7306 | 2024-11-17 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| d277d1a0-bc99-3edd-9e1a-5fd74b6f0b1e | -3.5309 | -50.2547 | 2024-11-17 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 0fbab383-0732-382b-b163-f373b0b8cadd | -3.0156 | -45.4128 | 2024-11-17 02:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 434fa9d3-647a-34f8-b235-43dc70923adb | -2.6595 | -46.2065 | 2024-11-17 02:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 22ffe5d5-2b8f-3fbb-8399-d165dafd30de | -2.2296 | -47.2316 | 2024-11-17 02:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 2056fb66-f640-3df9-852c-dc4252458ca4 | -3.5851 | -50.5255 | 2024-11-17 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 726b2295-82f0-3b92-99ec-e1f69484deab | -1.8981 | -46.5808 | 2024-11-17 02:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| d9337263-46f2-308b-9458-f0d46c50ae27 | 0.6159 | -51.7676 | 2024-11-17 02:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 90.1 |
| c9b83262-1d45-3621-8b84-301d7028d96b | -2.2111 | -47.2321 | 2024-11-17 02:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e6feb96d-962d-3e75-bcf2-6e223b280801 | -1.4888 | -47.3999 | 2024-11-17 02:40:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 4c9b824e-6e5a-372f-b818-da0123cfef5a | -2.5802 | -47.571 | 2024-11-17 02:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| fdb0bdbd-293f-36d0-b164-2cd070d52e49 | -8.4522 | -44.223 | 2024-11-17 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 591671d0-3c78-3b92-849c-5d144f82918a | -3.5124 | -50.2553 | 2024-11-17 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 8c4a4057-e42a-33fc-af6d-50c63f2fa294 | -3.531 | -50.2337 | 2024-11-17 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| b19353c4-142a-3c5f-a2b0-ef8dae31bd4e | -2.8615 | -46.7086 | 2024-11-17 02:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 20bc109a-f876-330f-875a-da0318c3cd7b | -2.6322 | -48.5634 | 2024-11-17 02:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| c469e3bd-3c3a-3dbf-aae5-a61faeb7c1d3 | -2.5988 | -47.5488 | 2024-11-17 02:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| b7b24684-fccf-3c55-9554-06174cc94209 | -2.5987 | -47.5705 | 2024-11-17 02:40:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0784b1de-afbd-32a4-911b-3adc99beffbc | -1.9167 | -46.5584 | 2024-11-17 02:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 2bfa6b06-f574-316b-8f8f-e7b424948076 | -2.678 | -46.2059 | 2024-11-17 02:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1ce5dafb-9b3f-3c52-b69e-6448ce852442 | 0.6159 | -51.7881 | 2024-11-17 02:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 67.9 |
| d28bf41c-58a6-3009-a61d-edb7a6f62f9f | -4.5616 | -47.9925 | 2024-11-17 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 082d7f99-b30b-3f8d-9612-9a9d10352c32 | -8.4333 | -44.2251 | 2024-11-17 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 18061c9d-8440-3457-bd19-32917ec05328 | -4.5614 | -48.0141 | 2024-11-17 02:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 3c3acae3-9bf6-3d56-8220-44da1882fe6d | -8.4528 | -44.1767 | 2024-11-17 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 579f709f-e6ad-3ebd-afd3-eef872af4b53 | -3.3359 | -52.7847 | 2024-11-17 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2e0fb8ec-4639-339b-a079-7b11706aaa23 | -1.9166 | -46.5804 | 2024-11-17 02:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 6708780b-ff31-34dc-9d18-82e5cebc7357 | -8.4336 | -44.2019 | 2024-11-17 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 449.4 |
| cd3d8cd7-763f-36d1-9da5-b743dd2b60eb | -2.2111 | -47.2102 | 2024-11-17 02:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| b6b06aec-9dc3-3759-b18c-4531d029d302 | -3.3359 | -52.7643 | 2024-11-17 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| a6ccb684-ad08-3991-b335-c5dd722e70f4 | -8.4339 | -44.1788 | 2024-11-17 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 99ffc0b5-9089-3169-9f06-45f66a8ed986 | -3.3175 | -52.7648 | 2024-11-17 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0cc2eb80-4460-31a6-8c78-1b803d9a9c38 | -8.4525 | -44.1999 | 2024-11-17 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 572.9 |
| 5e9c28de-6a26-3a25-af2b-5a0a48fdd5be | 0.6159 | -51.7881 | 2024-11-17 02:50:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 54.7 |
| bfd2928d-c120-3058-a7bd-3a37c5a2998e | -3.5309 | -50.2547 | 2024-11-17 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 373.4 |
| b7fc3d97-cab4-3806-8667-a8d9cd4b5dd6 | -4.4101 | -45.5293 | 2024-11-17 02:50:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b7f4451a-17b4-33d4-99b1-0cf83b722864 | -2.2296 | -47.2098 | 2024-11-17 02:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| d2d39eb4-e8fe-3418-a4c3-6479231bffd2 | -4.5616 | -47.9925 | 2024-11-17 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| f17fae1b-6d98-30b6-afaa-95a3479c2836 | -4.5614 | -48.0141 | 2024-11-17 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 5f36f2da-ed54-3c0b-ae04-a7d1648ad902 | -2.8615 | -46.7086 | 2024-11-17 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| a70c376b-4ffe-3773-bac5-2e598820a88b | 0.6159 | -51.7676 | 2024-11-17 02:50:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 3a1ea9cf-7643-347f-a769-4522c1101fff | -3.5308 | -50.2757 | 2024-11-17 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| d65cdf51-4dc2-3a09-a8f8-530dd0b8b2de | -8.4339 | -44.1788 | 2024-11-17 02:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 135.2 |
| fd5c59cc-80bd-3ec2-9ffc-443e63b9d48c | -8.4336 | -44.2019 | 2024-11-17 02:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 338.8 |
| 9c6892dc-b2ca-3037-847a-0971485659a8 | -3.531 | -50.2337 | 2024-11-17 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 568dc120-39d5-37db-8761-d758acec3825 | -8.4522 | -44.223 | 2024-11-17 02:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 173.1 |
| c9bc03f4-a1ee-3272-bd26-d1da905cc3b9 | -3.5494 | -50.254 | 2024-11-17 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 714882d5-f76a-3ffc-b2e1-d7e63bca5020 | -8.4525 | -44.1999 | 2024-11-17 02:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 674.3 |
| 6ce67729-06d0-3ac8-9716-1d37ad69d767 | -2.6322 | -48.5634 | 2024-11-17 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 8ba663cc-b16a-3694-814e-fa72490ac008 | -2.2296 | -47.2316 | 2024-11-17 02:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a0bc2f65-5717-3d67-8703-5abcb94e02e7 | -8.4333 | -44.2251 | 2024-11-17 02:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 10784db4-5d4e-3df6-96ed-f121f28174dd | -1.9166 | -46.5804 | 2024-11-17 02:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 6d60a047-48bc-3f66-80e3-81a4764bb4ed | -3.3359 | -52.7643 | 2024-11-17 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| dd651072-f959-3f2c-bde9-c857d6c88a1c | -3.3175 | -52.7648 | 2024-11-17 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 6e608059-ece9-36a1-bba3-96d0339fe45d | -2.678 | -46.2059 | 2024-11-17 02:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2549ec59-e53a-3618-b9f4-69f76c67ec63 | -8.4528 | -44.1767 | 2024-11-17 02:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 295.0 |
| ae902841-3c8f-3357-95a5-cc3761c06724 | -1.9167 | -46.5584 | 2024-11-17 02:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 53c5594f-f10a-34af-b6bc-6e3fb1bbca4f | -2.2111 | -47.2321 | 2024-11-17 02:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 011e0f22-2e28-31b5-a8b8-20559b93cfdf | -2.5988 | -47.5488 | 2024-11-17 02:50:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b01262ae-b9da-3fea-a9b9-421c26debbf4 | -3.5124 | -50.2553 | 2024-11-17 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 562cb9da-9f27-3b9c-b8df-8d54caf63c75 | -2.2111 | -47.2102 | 2024-11-17 02:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 52c263bf-9337-391e-a63d-566efad4d87e | -2.8614 | -46.7306 | 2024-11-17 02:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |


[Clique aqui para ver as próximas entradas](README20.md)
