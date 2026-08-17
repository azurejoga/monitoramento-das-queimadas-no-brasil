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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dabdc34-cf5c-35b0-87b4-2f8342192697 | -6.6199 | -58.9643 | 2026-08-17 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 0351bc7d-c3da-3512-a70f-b8171ec2da45 | -15.8994 | -55.5334 | 2026-08-17 01:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fb6ae239-165d-3059-97ab-999a1bce6a7a | -15.9298 | -47.8334 | 2026-08-17 01:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8b5d5639-c975-34f2-9c64-9617c486b1a1 | -14.4739 | -45.6682 | 2026-08-17 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1c7b36f2-7b75-3d2e-b044-aadf4f4ab0c2 | -8.9038 | -60.5962 | 2026-08-17 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| f4988474-9fe7-34da-8e9c-00c60d03fcb8 | -14.4934 | -45.6647 | 2026-08-17 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| ad3ceb68-03b5-339d-8bec-aaffe9cab631 | -8.9787 | -60.5156 | 2026-08-17 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 33f4f03e-8fb8-3191-aa27-ca633f53f9e4 | -7.3824 | -55.4924 | 2026-08-17 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 186756b7-ba8c-389d-908e-d9cd4488d8c9 | -6.6938 | -58.942 | 2026-08-17 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d9d240ab-1e12-3663-af58-b661ac56d006 | -8.9041 | -60.5577 | 2026-08-17 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 322c8bee-5d02-39dc-9383-82275a20e9d9 | -6.6384 | -58.9636 | 2026-08-17 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| aff9e979-fa7b-30ed-912b-196846561a77 | -6.6014 | -58.9844 | 2026-08-17 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 49e2383f-53dc-3cf0-ad27-732dcd9d0c3d | -6.6015 | -58.9651 | 2026-08-17 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a89def6e-5f26-3cf1-ac48-11d4349bc200 | -15.9495 | -47.8299 | 2026-08-17 01:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 86abb43f-f87a-3642-b8d5-7b56c392d6c7 | -6.1106 | -57.7425 | 2026-08-17 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| f549fedc-5622-334a-a1bd-48c6b3b27353 | -6.1107 | -57.723 | 2026-08-17 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 493b45e2-f77c-3266-9543-3b867c9877ba | -6.6568 | -58.9628 | 2026-08-17 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5afbf2b7-1230-3749-a17e-9dbbf7add099 | -15.949 | -47.8526 | 2026-08-17 01:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 876ae330-028d-36a4-b326-dd1cdfeafaaa | -6.7123 | -58.9412 | 2026-08-17 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| de69b2ef-4f17-3e36-92fa-ca173aa92ac5 | -6.6568 | -58.9628 | 2026-08-17 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c7b858d5-2224-3f1f-8244-1f1ce607b052 | -6.6199 | -58.9643 | 2026-08-17 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a655b158-3c01-3324-8865-6e512a01a6a4 | -14.7173 | -47.9728 | 2026-08-17 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 210.8 |
| 620b32fa-0b6b-32ba-b094-b1609f37e84f | -10.4658 | -50.3907 | 2026-08-17 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 3e8337ce-8a33-3377-9731-b32bd553508f | -8.9041 | -60.5577 | 2026-08-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0a2cf529-8687-338d-b821-643f0aa9e38c | -15.8994 | -55.5334 | 2026-08-17 01:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| da212998-e1e4-3190-b08a-a0da1b20615c | -14.6983 | -47.9535 | 2026-08-17 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9e70ca14-0322-377e-b5f4-52caa0643723 | -7.3824 | -55.4924 | 2026-08-17 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 8bd0ada7-9349-37f6-8855-606cf376795a | -14.4934 | -45.6647 | 2026-08-17 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c62911bf-ec3f-3104-b6e2-ab0120524fd1 | -8.9787 | -60.5156 | 2026-08-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 06f3864f-f981-3271-85d9-de7c897768b1 | -10.4655 | -50.412 | 2026-08-17 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| cb708639-0e30-376a-ad1e-97d49bccd542 | -14.6978 | -47.976 | 2026-08-17 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cadcc3f8-864c-3fdb-8f66-a93f1fa9e536 | -14.7178 | -47.9503 | 2026-08-17 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 9d2e17b1-4514-30a4-8cee-f476e97e8642 | -14.7373 | -47.9471 | 2026-08-17 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 37.5 |
| bae641b6-fba5-3815-9eff-1ec8b544756c | -6.1106 | -57.7425 | 2026-08-17 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 551a6e74-0505-3669-8973-c07092d4ae70 | -6.1107 | -57.723 | 2026-08-17 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| e8bd684b-143e-3082-85aa-c5db8f7d8fbc | -6.6015 | -58.9651 | 2026-08-17 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f8394ba6-4174-301f-b180-9292687f4f5b | -6.6014 | -58.9844 | 2026-08-17 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 8896f4d4-aaeb-3ab2-9cf0-bc3bae8ee35b | -14.4739 | -45.6682 | 2026-08-17 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 62458a8e-b26a-31e7-9c78-024cc8c64e75 | -15.9495 | -47.8299 | 2026-08-17 01:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 78f18992-66ff-30ec-9735-fb4561428c9c | -8.9038 | -60.5962 | 2026-08-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5d42de3f-66bc-316e-8703-f204b3e4709f | -14.7368 | -47.9696 | 2026-08-17 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |
| b3b1326f-1351-33b3-a7d5-617ea0b453d4 | -6.6384 | -58.9636 | 2026-08-17 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| db148102-f8c0-380a-9d6a-724a8d5acade | -14.4934 | -45.6647 | 2026-08-17 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 62e3cf74-8994-379e-88ce-6348eec1617f | -10.4658 | -50.3907 | 2026-08-17 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 569979cc-a412-3379-ad82-25796e4f4a0d | -7.3824 | -55.4924 | 2026-08-17 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b314355e-3e51-3078-bb75-24058476b471 | -14.4739 | -45.6682 | 2026-08-17 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 50a58bbc-f5d5-3e0a-9cfb-b3d8dbdff163 | -15.9687 | -47.8491 | 2026-08-17 02:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 47.8 |
| bc787e68-88bd-357c-86d0-29f66c31bb21 | -15.9692 | -47.8264 | 2026-08-17 02:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 50.9 |
| ae5ced96-4202-342d-b82c-99e16c76c6f2 | -6.6384 | -58.9636 | 2026-08-17 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| ff48e19c-f111-3cc9-8b2e-800fbbb93c96 | -6.7123 | -58.9412 | 2026-08-17 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 66e1b62e-6ffb-3dac-a03e-0c11d18575bd | -15.9495 | -47.8299 | 2026-08-17 02:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 186.9 |
| c0ebdbd6-d68d-3697-a1ad-136027c232cf | -6.6199 | -58.9643 | 2026-08-17 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 96fedbd6-d13a-3a81-bd7e-3b0e15a0e654 | -6.1106 | -57.7425 | 2026-08-17 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 71fefbb3-6a54-3a68-957d-33f1594fc1f4 | -8.9038 | -60.5962 | 2026-08-17 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e5e08468-e3d0-3dd0-84ae-aea11ca5cd43 | -15.949 | -47.8526 | 2026-08-17 02:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 91746517-fade-3de1-ac9e-184b1c3fcc95 | -6.1107 | -57.723 | 2026-08-17 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 47efe506-2a2d-31f4-be39-c180b28498a6 | -15.9298 | -47.8334 | 2026-08-17 02:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 7e1bd4d5-17ee-3f4c-bb13-d3f5045af52b | -8.9041 | -60.5577 | 2026-08-17 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c959b8a6-5e78-397c-b1eb-ef5a972c93bb | -6.6015 | -58.9651 | 2026-08-17 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4e670c52-0be3-31ba-b537-38c8d1d07e15 | -6.6568 | -58.9628 | 2026-08-17 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2c1fe7ab-dd7c-3e16-82bf-0c13d7f3ffc2 | -11.8083 | -44.8072 | 2026-08-17 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 395a9ff5-97b6-3cc6-b9a4-a1781350cb15 | -6.6568 | -58.9628 | 2026-08-17 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 704dbab6-d039-37f3-aef5-bb6463f80fbd | -6.1106 | -57.7425 | 2026-08-17 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| e2397781-1068-3834-9753-3c7ff4096d43 | -6.6015 | -58.9651 | 2026-08-17 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4ddf867e-e393-31ff-9767-21350e5e846e | -6.6199 | -58.9643 | 2026-08-17 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d99adf0e-ea3c-3b9d-9443-3b462001f0a7 | -6.6384 | -58.9636 | 2026-08-17 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 31be0edf-87d4-3541-b26c-6274b00f7943 | -8.9041 | -60.5577 | 2026-08-17 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 73076730-a454-3e5a-b836-c64b65059828 | -15.9495 | -47.8299 | 2026-08-17 02:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 216.6 |
| b84777e1-ed99-35b3-8551-951562c396d8 | -14.4739 | -45.6682 | 2026-08-17 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 9118266b-c7da-3a7e-a42f-19699499d701 | -6.1107 | -57.723 | 2026-08-17 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| de9ec60f-3784-31e8-a01e-d4f417234633 | -6.7123 | -58.9412 | 2026-08-17 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 51b6e45f-be21-39b2-b96f-06a143d7ab10 | -10.5088 | -50.0013 | 2026-08-17 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 469921cd-6537-3cd0-aa59-4b20b047aa26 | -15.9298 | -47.8334 | 2026-08-17 02:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 46998fde-b749-397c-84f7-eaa3f46ae61e | -7.3824 | -55.4924 | 2026-08-17 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 89bdc300-1cd4-31d8-a92b-767a4ae98297 | -14.2754 | -53.1076 | 2026-08-17 02:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 1a48e601-d8cb-3cda-808d-1e47a84904aa | -15.949 | -47.8526 | 2026-08-17 02:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 8be8e197-dbd0-30aa-8a2d-97f250546f32 | -15.9293 | -47.8561 | 2026-08-17 02:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 51c1464d-7b7e-3bb9-ba70-8a83ac4004c8 | -14.2751 | -53.1287 | 2026-08-17 02:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 04d55477-72d9-314b-b66c-c191c4a63d76 | -10.5085 | -50.0228 | 2026-08-17 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| b6c0a1bd-8994-326b-8193-455cc10434aa | -8.9038 | -60.5962 | 2026-08-17 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| db6f09a4-c976-32a0-978e-4dacd6c7576f | -8.9038 | -60.5962 | 2026-08-17 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| fa339ca3-a8da-3714-b79e-5deee66ab994 | -6.1106 | -57.7425 | 2026-08-17 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 9c4dfbef-101e-3a12-b2e6-476a387f007d | -7.3824 | -55.4924 | 2026-08-17 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 839601b4-f2bc-3435-8ca3-f9889bfe8af2 | -6.6568 | -58.9628 | 2026-08-17 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 6730a948-e89a-32cb-accc-9d52f4866930 | -8.9041 | -60.5577 | 2026-08-17 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 999f7fd9-17ef-31e6-9fee-ccf488527a9b | -6.7123 | -58.9412 | 2026-08-17 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 4a03ac5b-92ca-3200-8d93-0fa95f79c9fb | -6.6199 | -58.9643 | 2026-08-17 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| b8c720e2-2a67-31cd-9b5e-2687dccb3a7d | -14.4739 | -45.6682 | 2026-08-17 02:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| f0dde530-1ea4-39f3-9635-1da25f408840 | -11.8083 | -44.8072 | 2026-08-17 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 5db433ed-802b-3c0e-b97b-5fe6a140d482 | -15.949 | -47.8526 | 2026-08-17 02:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 3671cac4-49e3-309f-ac70-503576c92016 | -15.9495 | -47.8299 | 2026-08-17 02:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 060139cc-f1d1-312b-ad41-a460cee8126c | -13.6436 | -56.9807 | 2026-08-17 02:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 6e86fb1a-f03f-338a-9e31-8c7bb2e0b0bb | -6.6015 | -58.9651 | 2026-08-17 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 5abf05af-6676-37a1-9a63-804cd4f9c64e | -6.1107 | -57.723 | 2026-08-17 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| f8e5d558-6a03-3d76-b2fb-04241385d1ab | -6.6384 | -58.9636 | 2026-08-17 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 5a6780cd-edb0-388d-90ba-d25e85fb361b | -6.6199 | -58.9643 | 2026-08-17 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 41464db5-af1e-3978-9556-281e30385752 | -8.9041 | -60.5577 | 2026-08-17 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4c2810cb-d573-3b4b-bf02-85aec5e0bea2 | -7.3824 | -55.4924 | 2026-08-17 02:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 7031b99c-1277-30e8-9990-4bd3b8f6dbea | -6.6015 | -58.9651 | 2026-08-17 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 10fe2858-f835-332c-8142-126b24951625 | -6.1107 | -57.723 | 2026-08-17 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |


[Clique aqui para ver as próximas entradas](README9.md)
