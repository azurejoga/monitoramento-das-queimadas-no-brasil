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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7db72d08-0d0e-3463-812d-f9aff7e56035 | -8.9038 | -60.5962 | 2026-08-17 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 75958aae-7759-3eaa-a4e9-3537cf7b3e66 | -6.6568 | -58.9628 | 2026-08-17 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 686255be-a38e-32cc-968e-4ab88d5033c2 | -6.7123 | -58.9412 | 2026-08-17 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| da3d3a32-5494-3f9b-9d48-0f85b7211698 | -11.8083 | -44.8072 | 2026-08-17 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 4b80e8ee-25c6-3e52-bd3e-d0e9c00cf159 | -6.1106 | -57.7425 | 2026-08-17 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| b39e7648-5801-332d-8543-7adee66cc142 | -15.949 | -47.8526 | 2026-08-17 02:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 555ce97a-97f4-358e-94a3-7359208748c4 | -15.9495 | -47.8299 | 2026-08-17 02:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 32d47d3b-c181-31f5-b787-763e66df561b | -6.6384 | -58.9636 | 2026-08-17 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 6ebe9fe0-3435-3875-9741-ae742de9978f | -13.6433 | -57.0009 | 2026-08-17 02:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 731a2e41-85cd-3a10-b58e-e65bf192fb04 | -7.3824 | -55.4924 | 2026-08-17 02:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 134ee449-d54e-3692-b72b-62ce969366b2 | -6.6199 | -58.9643 | 2026-08-17 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b77c9da0-58c9-37d5-9473-3c4c5a126610 | -6.1106 | -57.7425 | 2026-08-17 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| e674b2f4-e1be-3849-8687-d6e8ef9b2ed3 | -6.6568 | -58.9628 | 2026-08-17 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| eb671374-31b7-39b3-b80e-586674ac4d61 | -8.9038 | -60.5962 | 2026-08-17 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0b074409-6fe8-30c9-95de-1cd6b11172ce | -6.1107 | -57.723 | 2026-08-17 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 2be8c2e8-ebe7-362d-b653-0f2c30088910 | -8.9041 | -60.5577 | 2026-08-17 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| dff45784-1ba6-3a61-9e8c-a77cc4b04d39 | -6.6384 | -58.9636 | 2026-08-17 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| f0710b6d-33c2-32e7-8059-7b7b41bdaa5d | -6.6015 | -58.9651 | 2026-08-17 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fd68bb13-d447-3f9c-bc70-e2e33b80937c | -6.7123 | -58.9412 | 2026-08-17 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| dcac91e4-2eac-3da1-8f0e-c99bc5e4bfc3 | -14.4934 | -45.6647 | 2026-08-17 02:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e9958db2-4539-329a-8b7f-ee2163fcfa32 | -15.9495 | -47.8299 | 2026-08-17 02:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 0471c6ee-5e5c-33c4-961c-4eb9d2867114 | -6.6568 | -58.9628 | 2026-08-17 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 1212ac21-6495-3f25-a61c-34f176b7de8b | -11.472 | -46.5692 | 2026-08-17 02:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 7ccbcf4f-b9b5-37b9-b403-1e8253cde197 | -8.9038 | -60.5962 | 2026-08-17 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 53750852-66b2-30e3-a441-99053cc95bbc | -6.6384 | -58.9636 | 2026-08-17 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 6d9ce619-87a8-3f41-bbda-ad10884ac474 | -6.6199 | -58.9643 | 2026-08-17 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 01126c71-5760-33b2-a70b-0e999ff8dfa5 | -7.3824 | -55.4924 | 2026-08-17 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b4cabf12-07ea-3e4d-b3ac-d767fd30bc3c | -6.1107 | -57.723 | 2026-08-17 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 46503f71-ea91-3967-988d-cfd233c60b6b | -6.7123 | -58.9412 | 2026-08-17 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 272639bb-d189-3e8b-8b84-01c7984c75fc | -6.1106 | -57.7425 | 2026-08-17 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 50cc18c8-b09e-3288-886d-9f928e355cad | -14.4934 | -45.6647 | 2026-08-17 02:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 0eac78a1-396d-338f-babd-8aa49f59c8f7 | -7.3824 | -55.4924 | 2026-08-17 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1bd46b6b-30a1-320b-8884-e467588551ec | -6.6015 | -58.9651 | 2026-08-17 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 7221aace-1be1-3d29-aa7b-74ce29120609 | -8.9038 | -60.5962 | 2026-08-17 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| a916fded-2bc0-347f-982a-b6745a897fde | -6.6568 | -58.9628 | 2026-08-17 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 3661a3f6-f655-37ce-aa5c-43436f595b8a | -6.6384 | -58.9636 | 2026-08-17 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| d4121424-7dfe-3d57-9d19-2a41a4e113de | -6.1107 | -57.723 | 2026-08-17 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 63bff79c-8815-30ff-943c-b79b95e07bff | -6.7123 | -58.9412 | 2026-08-17 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| da755cf0-7212-3255-b256-558d158860e6 | -6.1106 | -57.7425 | 2026-08-17 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 155705d0-4459-366b-a890-466f8e2a4ef2 | -6.6199 | -58.9643 | 2026-08-17 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 93dd87cf-223c-3821-be3b-fd65af8c55b5 | -6.6015 | -58.9651 | 2026-08-17 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 976695c2-09e0-3d11-9b79-f12c29d9aa7a | -8.9041 | -60.5577 | 2026-08-17 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 5ea49319-81a1-386b-8dd3-63b16bb1d41f | -10.5085 | -50.0228 | 2026-08-17 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 989f5823-6165-3279-b377-c50793c85bfa | -6.6199 | -58.9643 | 2026-08-17 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 9361a345-04fd-31c6-ae01-0995e4c335e3 | -6.6568 | -58.9628 | 2026-08-17 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| a35fddfb-cfb0-3f01-9903-efdef73ec4a5 | -7.3824 | -55.4924 | 2026-08-17 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f108ead1-39eb-32cd-aec8-6823f80d09ba | -6.1106 | -57.7425 | 2026-08-17 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e66415ab-3c6e-3f17-8085-b055f70d01bb | -6.7123 | -58.9412 | 2026-08-17 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 45694550-b9b4-362e-ab4e-bbd12ff43027 | -6.6384 | -58.9636 | 2026-08-17 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 914c1827-c0b9-34d8-b1ac-5a15d5a772f4 | -8.9038 | -60.5962 | 2026-08-17 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f65a0789-ed8e-3546-9470-0ad92abb8e20 | -4.52278 | -38.54993 | 2026-08-17 03:15:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 14c800eb-2e52-339c-ab47-ffedc069bb77 | -4.5292 | -38.54968 | 2026-08-17 03:15:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 41706bc8-7da4-3312-94a5-8d88d76a0105 | -4.52965 | -38.55123 | 2026-08-17 03:15:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75ae9116-eae2-3bd2-aa13-ec6cf2aeaaa6 | -7.3824 | -55.4924 | 2026-08-17 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| dc26cb1a-9d5d-318a-8240-636a7aaf7e0a | -6.6384 | -58.9636 | 2026-08-17 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 9827f902-fe0f-3a98-8d64-97a3ccdbf8dd | -6.7123 | -58.9412 | 2026-08-17 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c5cc2435-2da2-332a-b1aa-a3c846f56ae5 | -6.6568 | -58.9628 | 2026-08-17 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 5c8b57e4-d7de-3de1-8d89-0110fad0a5af | -6.6199 | -58.9643 | 2026-08-17 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| fc267cf3-3277-3800-96dc-1f1bc33edb92 | -6.6568 | -58.9628 | 2026-08-17 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| ab3c4318-4be5-3cc8-9dc8-a15cfd083a32 | -16.4204 | -49.6274 | 2026-08-17 03:30:00 | GOES-19 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 4db57725-304b-351d-97da-97040928e7ca | -6.6384 | -58.9636 | 2026-08-17 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 3d6a4ea0-f8a1-37c2-909a-094d637e04c0 | -6.6385 | -58.9442 | 2026-08-17 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7f4f1a08-06ad-3b27-86ef-e298e792c140 | -6.7123 | -58.9412 | 2026-08-17 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 8d9b3c5f-1bfa-3da0-8472-fecf0cc52b10 | -6.1106 | -57.7425 | 2026-08-17 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 96305f08-08b0-32ff-9d94-eebce96a985d | -6.6199 | -58.9643 | 2026-08-17 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 1532bf7c-805a-3dec-bb2a-4fd083e2995e | -15.9189 | -55.531 | 2026-08-17 03:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0ba99c34-bbfd-313b-a449-b33ef246bfab | -15.8994 | -55.5334 | 2026-08-17 03:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 736bcecf-be5c-375d-a630-933782141c18 | -7.3824 | -55.4924 | 2026-08-17 03:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 1ad7d82a-ff9c-3ddd-b5b7-7f3393c7ee7f | -8.9041 | -60.5577 | 2026-08-17 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 47bd8e28-9bfc-3d6c-8853-f7bafed6c37d | -8.9038 | -60.5962 | 2026-08-17 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1b6e07a1-5411-379c-86d1-f5309f834975 | -6.6015 | -58.9651 | 2026-08-17 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 062fb31d-839f-3bfd-9a91-410cba3183e1 | -6.18863 | -39.26676 | 2026-08-17 03:34:00 | NOAA-20 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3ae0465c-b515-3507-a407-60cd3e5a278a | -3.92335 | -38.43706 | 2026-08-17 03:34:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8f083d8-deed-3e5d-baee-35162a1bb735 | -4.52617 | -38.54721 | 2026-08-17 03:34:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5d40eb99-e5ed-39b0-bc16-10d9756c2e0c | -5.69697 | -36.25281 | 2026-08-17 03:34:00 | NOAA-20 | LAJES | RIO GRANDE DO NORTE | Brasil | 2406700 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 818b5cec-6ae8-3b8d-88dd-a4a49d0b36df | -4.5254 | -38.5518 | 2026-08-17 03:34:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bd6377b0-aff9-39bf-b935-bd904283c239 | -3.96203 | -43.10521 | 2026-08-17 03:34:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7bf54eb-0763-3493-b97a-fb4f5243bd11 | -6.21611 | -38.23623 | 2026-08-17 03:34:00 | NOAA-20 | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| dc3bcb49-ff58-3708-9baa-ade0ee7ec178 | -11.13252 | -46.51536 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05676f36-0f9e-33f0-9c49-b2bc8b241e6b | -6.53419 | -43.11272 | 2026-08-17 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbaae64e-f6e5-3189-af40-5c18f4a52cf9 | -11.47889 | -46.57772 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6fd2ccbe-4ce4-3177-8852-963a8e990877 | -11.49095 | -46.58712 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc28dc9e-34be-3e5d-8bdd-7d47e308811d | -11.44685 | -46.58728 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e08c1cf-deb3-349f-b5a9-f3527f454f36 | -6.53257 | -43.1217 | 2026-08-17 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb86568f-c1b3-3e85-8b79-01fdb7e01cd7 | -6.30915 | -43.6217 | 2026-08-17 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b64f74ca-c74e-387a-bfea-16c33889770b | -11.80732 | -44.8133 | 2026-08-17 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7ab46932-5b6b-3a64-aa02-5396e8f379e0 | -6.52664 | -43.12056 | 2026-08-17 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 594aaad9-bf4a-31c4-9ab6-b37039d142c7 | -9.75321 | -47.23259 | 2026-08-17 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 90c4998a-6b35-36e5-b5d9-d58825b51690 | -10.46259 | -46.3005 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f45d166-fc43-3c7e-a4d3-e1cefc976d4a | -6.52745 | -43.11605 | 2026-08-17 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 29ee0fc8-ddd2-3ce5-8f74-91fc23c2719a | -11.13122 | -46.52171 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fa37616-ddfe-3548-b47a-26f1bdfa7951 | -8.73095 | -45.31165 | 2026-08-17 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6320934c-163f-3522-bea3-e172361f99ba | -11.46375 | -46.58291 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 153e480f-f3e9-3208-a7cc-c1ff09dc6907 | -11.09685 | -47.29617 | 2026-08-17 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2574d07-c70a-3f01-8401-5d51eb1cfbe9 | -11.39075 | -46.4053 | 2026-08-17 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 097f78c7-bcfd-3b66-bffa-e255d267bd18 | -8.73211 | -45.30579 | 2026-08-17 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d8931d8-df28-33c6-8e2a-c78650b23142 | -11.81335 | -44.81457 | 2026-08-17 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a70cc4d-e974-3353-88aa-3e1f2149e586 | -11.09988 | -47.29755 | 2026-08-17 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1609f493-68d4-3669-948b-ad197397a085 | -9.12018 | -45.17684 | 2026-08-17 03:36:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b880c7c1-e2c1-32ea-9c36-04563d7dd163 | -11.31675 | -46.31043 | 2026-08-17 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README10.md)
