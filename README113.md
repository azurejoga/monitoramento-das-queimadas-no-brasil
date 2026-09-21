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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 829102a1-5b33-31d4-9fff-c9d0eaeec46c | -7.4092 | -44.7885 | 2026-09-21 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| a301bd42-761c-3175-ad02-4e1c31af3ebc | -12.8899 | -50.9695 | 2026-09-21 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| df8af492-eeb5-3b42-b187-da87676eae76 | -11.041 | -54.1567 | 2026-09-21 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 3c859322-90c6-3975-a5b1-be5afef11158 | -9.8307 | -48.451 | 2026-09-21 12:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 52971102-7e10-306e-a42d-a490b821d39c | -8.7537 | -44.2821 | 2026-09-21 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 9578e843-6366-3369-a0d5-97da72a7b93e | -10.8011 | -50.7604 | 2026-09-21 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| dbe696cd-a533-3172-b934-18ce62573212 | -9.4567 | -45.4178 | 2026-09-21 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b3c36378-7e1c-37e4-9a7c-3208132411c1 | -7.4124 | -49.853 | 2026-09-21 12:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| aa05d23c-b78d-33fc-a670-240a8573f8b9 | -7.5661 | -42.656 | 2026-09-21 12:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 63e5bafa-210a-3a6b-aea6-2d4d0654c9e3 | -11.8495 | -46.833 | 2026-09-21 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| d14c2b42-edee-3ec0-a2c9-f91e0155f9fb | -12.9091 | -50.9672 | 2026-09-21 12:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 4930220e-9361-3a81-965e-37532506c144 | -6.8263 | -55.5421 | 2026-09-21 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 3cb4bd96-f84b-343a-8813-6de337af5390 | -10.744 | -50.7876 | 2026-09-21 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5d86cdb6-96c7-3d98-a458-a66173a0c3cf | -10.3917 | -48.8915 | 2026-09-21 12:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 92b281db-7f03-39d8-a3d0-73bee27d40f7 | -8.7911 | -48.7502 | 2026-09-21 12:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 5abb1521-9cb9-33ec-91be-899aefd75558 | -10.8197 | -50.7797 | 2026-09-21 12:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| a0f62d1a-16a5-3340-9699-ba539fcd7b23 | -13.9118 | -48.5669 | 2026-09-21 12:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 98c8d350-7220-36d5-b155-012c6f2f79f9 | -12.8434 | -54.0629 | 2026-09-21 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 14c14fef-0653-31e1-9f1a-ce1a8f457892 | -10.4675 | -50.2624 | 2026-09-21 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6a67bf70-9b40-3e4b-a07e-599e9dbaccca | -6.8448 | -55.5411 | 2026-09-21 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 174.3 |
| 13eeb2bd-836b-3ca5-90a6-fd472b2f5ebc | -12.8246 | -54.0442 | 2026-09-21 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 178.1 |
| f331f3d8-1ec6-30e7-b55b-0f519a61c8a3 | -8.7726 | -44.28 | 2026-09-21 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 12264a21-8875-356d-b2ea-d15c91756664 | -7.428 | -44.7867 | 2026-09-21 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| abc8f456-1bb5-3559-a354-a1b1789f177e | -8.7729 | -44.2568 | 2026-09-21 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8367d450-dd11-35f0-84dc-d48416201ff1 | -10.3728 | -48.8936 | 2026-09-21 12:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 103f44b4-b7d9-3135-9d9c-7c9c4847fd38 | -8.754 | -44.2589 | 2026-09-21 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4879805c-29cb-3f76-b95d-5f35066f10c7 | -12.8437 | -54.0422 | 2026-09-21 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 255.6 |
| c57eddd1-f5be-334b-b62d-3437cf156cc5 | -7.3291 | -55.1955 | 2026-09-21 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 6c07893c-e62e-3749-a01e-e3463eb585a9 | -10.744 | -50.7876 | 2026-09-21 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 32364a2f-cabb-3e3b-b872-e3ac0d5bdf75 | -9.8694 | -48.3814 | 2026-09-21 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4da9be8c-b65e-3b48-b960-6e35e8e0b968 | -8.4922 | -47.0257 | 2026-09-21 12:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c36d4442-b693-3b55-b32c-7e56bc23b2ad | -7.5661 | -42.656 | 2026-09-21 12:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 136.6 |
| dbd3cbe6-dd17-3570-bbe8-eb54b585cdd5 | -12.4204 | -47.0228 | 2026-09-21 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| df10424e-3ed9-3683-a0a0-a4487a0c4bfc | -12.9091 | -50.9672 | 2026-09-21 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.7 |
| dfd6ce97-c2be-37ae-93f3-625886084f05 | -10.7064 | -50.7703 | 2026-09-21 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 0b5dd500-b6f7-3f76-85ce-05aa54f20cf1 | -11.9967 | -58.0821 | 2026-09-21 12:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| f32cb046-d255-3b5b-9559-40e1055005df | -10.3728 | -48.8936 | 2026-09-21 12:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| daddb62f-5c03-39b2-9f55-a1a808baa929 | -11.8682 | -46.8529 | 2026-09-21 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| f169f8e4-3151-3c1c-b326-e5fb41498aa1 | -12.2723 | -50.1657 | 2026-09-21 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| fa23e4d9-7e53-35d7-ba6a-efcbeb593fa5 | -6.2026 | -57.7778 | 2026-09-21 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 70000d2d-ee82-3e7f-b813-4971e5a0af6b | -8.7726 | -44.28 | 2026-09-21 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 9a2239d5-d429-3ddc-ad76-6962bfb4af3c | -9.8307 | -48.451 | 2026-09-21 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| a0fec9b5-a869-3f4c-a37a-6418b96e1826 | -16.01 | -52.5377 | 2026-09-21 12:20:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| b8ca8f41-625d-3e61-ad25-bb67bd52c0ea | -16.0495 | -52.5106 | 2026-09-21 12:20:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 2866dabf-1c94-3292-9de9-8dc334fecc11 | -10.3924 | -50.2275 | 2026-09-21 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0e5502d7-d6ed-30fe-b9e3-51762a4022fc | -8.7911 | -48.7502 | 2026-09-21 12:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 13cc132a-4ce5-354e-a37e-2e9f6c9aca2b | -7.3291 | -55.1955 | 2026-09-21 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 1a015812-a6c5-3acd-a5e7-d97afd082763 | -9.8692 | -48.4033 | 2026-09-21 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 311.3 |
| 033a9296-2f86-355b-953a-44c3fdaae9e7 | -7.4124 | -49.853 | 2026-09-21 12:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 9cd44a62-f57d-3e2c-b7f0-3f2efeca17e9 | -10.8197 | -50.7797 | 2026-09-21 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 4733df32-1b54-3f3a-96db-671252147021 | -11.9969 | -58.0622 | 2026-09-21 12:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a40fa6e7-84fd-3b61-b4f3-a4cde931b562 | -8.7537 | -44.2821 | 2026-09-21 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 156.4 |
| aa92a33f-aa42-360f-a28b-7247d77cf16f | -7.4092 | -44.7885 | 2026-09-21 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 6e9a2e87-7eb0-3680-9a7a-2891f58541e4 | -7.3289 | -55.2155 | 2026-09-21 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 74a3b1d0-13eb-35e3-a588-05dfea8b2003 | -8.754 | -44.2589 | 2026-09-21 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c0c8ec79-f56a-31e2-a4a8-d9bf6c60c829 | -7.4126 | -49.8317 | 2026-09-21 12:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| a825839b-a800-3458-874a-bc12b5e55c66 | -10.4297 | -50.2663 | 2026-09-21 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 7e3511bd-a696-346f-82a2-8736b735d072 | -10.8011 | -50.7604 | 2026-09-21 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| f42c88f9-3739-35b5-ba0b-4bb36eb66eef | -16.03 | -52.5135 | 2026-09-21 12:20:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 85f16b64-c52f-3a1a-8beb-7859aeedea96 | -12.2914 | -50.1633 | 2026-09-21 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| df654950-5307-3b7e-96e0-94433554aa75 | -9.831 | -48.4292 | 2026-09-21 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4ea4d9ed-3f73-3749-9aa8-37d7b294f912 | -10.3917 | -48.8915 | 2026-09-21 12:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 59ac75ad-7ec5-34e3-919d-3ece93e118d5 | -9.8689 | -48.4252 | 2026-09-21 12:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 152f20ea-a4ed-361a-8b04-8f4fb6942c41 | -12.8899 | -50.9695 | 2026-09-21 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 37839286-821f-3c73-acd7-e6cc8cfa1938 | -10.4486 | -50.2644 | 2026-09-21 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 3a7bfe44-8a27-3459-9d21-309e8f07c56d | -6.8448 | -55.5411 | 2026-09-21 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ecd8b317-44d5-311b-8c86-018104714b20 | -10.8014 | -50.7391 | 2026-09-21 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 3a0bafd2-b3af-3e4b-8264-a0e56293fb3d | -7.428 | -44.7867 | 2026-09-21 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e84f1e52-c5ba-36ec-a579-3cae8412e80f | -7.3289 | -55.2155 | 2026-09-21 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| d4d5c54b-89e5-3961-84a2-3a65d4984482 | -6.8263 | -55.5421 | 2026-09-21 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ece51df2-ba1b-3969-845e-84544c393ad2 | -10.4675 | -50.2624 | 2026-09-21 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d98baec6-9f5e-342e-91a9-d8dd1e6030af | -10.3917 | -48.8915 | 2026-09-21 12:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 70d09845-9fcd-3b6a-b9c9-2cb69d9a0f29 | -8.7537 | -44.2821 | 2026-09-21 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 214.1 |
| b03d2dfd-27fa-3b37-ade8-c471200ba8dd | -10.8096 | -50.1407 | 2026-09-21 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 9954f687-ebb2-3495-a452-9483cb6aba50 | -11.8491 | -46.8556 | 2026-09-21 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ccbddc4b-c2c6-392c-8159-6c31bf28e775 | -10.3914 | -48.9133 | 2026-09-21 12:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6b6a9478-883f-3132-93da-f4462fb0fcad | -7.428 | -44.7867 | 2026-09-21 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b40e1109-90cb-3b7f-a5c5-389dcd77ff77 | -10.7064 | -50.7703 | 2026-09-21 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d993efae-783a-30ea-ad27-8883be57c997 | -7.8663 | -49.305 | 2026-09-21 12:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7e4b649f-601a-3740-bf1b-e0b17281a2cb | -10.7437 | -50.8089 | 2026-09-21 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4dae2c0e-bd57-3c96-95ad-daaff3c738dd | -11.0544 | -47.6733 | 2026-09-21 12:30:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 3cb45eee-f477-3dce-bf2e-89272ff92f6d | -10.8746 | -50.9227 | 2026-09-21 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 320231db-8991-33e7-a540-926183a5ad47 | -10.744 | -50.7876 | 2026-09-21 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e33f1e8c-4a23-3857-9ba6-cc36fd3fbb63 | -8.7729 | -44.2568 | 2026-09-21 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 8aa4c1c4-cc2e-3dea-9cb0-581f70c5b507 | -5.9334 | -59.9707 | 2026-09-21 12:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 856fbde3-c75b-3b90-8bb8-7c0823d136a4 | -7.5661 | -42.656 | 2026-09-21 12:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 152.5 |
| a3a97ba9-c5e2-32f5-a805-2f3cc721db32 | -7.3291 | -55.1955 | 2026-09-21 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 5befd9ed-28c9-3216-a163-2917da9fb44c | -7.4126 | -49.8317 | 2026-09-21 12:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 196.6 |
| 540052cd-a849-3011-b4be-0506ffec7902 | -11.8682 | -46.8529 | 2026-09-21 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 8161f07b-64f8-39d1-a835-4353d92997b8 | -10.4486 | -50.2644 | 2026-09-21 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 8701d151-6954-3666-8aed-2eefe2f51591 | -6.4741 | -48.441 | 2026-09-21 12:30:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 89.9 |
| eff24574-c7e7-3c59-8b6a-ef0bd3db7860 | -6.8448 | -55.5411 | 2026-09-21 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| ae3516ac-965c-3878-84d7-37f97f78ce19 | -5.9151 | -59.9522 | 2026-09-21 12:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 55a12df9-c10f-362b-8f09-c8c50a957763 | -11.9967 | -58.0821 | 2026-09-21 12:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 993b5919-14ea-33ba-ab86-af9f2ced4473 | -8.754 | -44.2589 | 2026-09-21 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 5ff109fd-8904-335a-abb2-37543963e16b | -8.7911 | -48.7502 | 2026-09-21 12:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 79.1 |
| cd7dc9df-1e39-39b6-907f-7192ab4c2c43 | -11.8495 | -46.833 | 2026-09-21 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 3c170c67-1ebf-3eeb-a053-0df94f62bf09 | -12.2914 | -50.1633 | 2026-09-21 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8e2c7302-c3bf-3268-aa9c-e3d23a5ef730 | -12.8899 | -50.9695 | 2026-09-21 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 223.1 |
| d396dede-dede-36c6-8722-ca4e60d4e465 | -12.4204 | -47.0228 | 2026-09-21 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 146.6 |


[Clique aqui para ver as próximas entradas](README114.md)
