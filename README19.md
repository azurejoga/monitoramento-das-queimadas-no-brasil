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
| 6b323640-a5ec-39ce-9f5b-00c40a38df40 | -14.2247 | -45.5036 | 2025-06-30 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| cce667c6-077d-30e2-bee5-fccbe76e3f6f | -7.7133 | -47.8453 | 2025-06-30 13:20:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| cf09cd49-5162-3cf9-b801-a407b1a6dbaa | -11.5812 | -44.6554 | 2025-06-30 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| fa701eee-5845-3e14-bc48-a35ec1eac9a7 | -10.8573 | -53.7425 | 2025-06-30 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| a813f4e2-b0bb-349c-aa05-221f25252358 | -10.1112 | -51.5683 | 2025-06-30 13:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 997faaf3-98db-3c13-90f6-8cf1ef2498f9 | -14.2242 | -45.5269 | 2025-06-30 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| b84740d1-0e3d-328d-9b43-6e47b5ae289f | -10.8573 | -53.7425 | 2025-06-30 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f3eca80b-2624-3825-b4d8-338f81beef51 | -11.5812 | -44.6554 | 2025-06-30 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 64336bfa-7fe5-3dc5-a3e3-dc9c1ee5cadb | -14.2052 | -45.507 | 2025-06-30 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 274.6 |
| 5d58e2c6-8f26-3289-884e-134f2ed46a0f | -7.7133 | -47.8453 | 2025-06-30 13:30:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| ebc03c4f-2bd3-3685-8e28-32ffedd97669 | -11.5779 | -44.8413 | 2025-06-30 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| f5ac357b-6189-3575-a7eb-158ded897a26 | -14.2247 | -45.5036 | 2025-06-30 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| edbcfff6-ae51-3ca6-811e-e472c6450440 | -8.5722 | -51.5761 | 2025-06-30 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e99b03a2-10e9-3d57-bba7-007b92d753c0 | -11.546 | -47.8772 | 2025-06-30 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c95d09c8-912a-3379-b634-dfe824328544 | -11.6004 | -44.6525 | 2025-06-30 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 60124bf0-e523-3c59-9200-14b4822524ef | -11.546 | -47.8772 | 2025-06-30 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 12a628f3-8805-314e-a5de-67fa212e8998 | -7.7133 | -47.8453 | 2025-06-30 13:40:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| f73f79ba-da35-3ea2-b47c-6eecdf77f962 | -14.2242 | -45.5269 | 2025-06-30 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 3f81de95-b683-3267-8a84-784da68496a2 | -14.2247 | -45.5036 | 2025-06-30 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 75a2a8ef-3c7e-33ee-9bfe-42d3ace7d864 | -8.5722 | -51.5761 | 2025-06-30 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 6d758c00-62c3-3183-bfdf-91324c813906 | -11.5779 | -44.8413 | 2025-06-30 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 89c3070e-148c-364e-933c-da1f9b5d8505 | -12.9198 | -48.0686 | 2025-06-30 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4c6ca89c-130f-321b-a47b-f4e78a6b948c | -10.8573 | -53.7425 | 2025-06-30 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| dbfad356-1fb4-39b9-a7b0-392e7c7d2c89 | -14.2052 | -45.507 | 2025-06-30 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 219.7 |
| 447e93e5-a196-3d4b-838b-512107b5ee5c | -10.1112 | -51.5683 | 2025-06-30 13:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 6ea54447-fc9a-37e7-bcde-893731e16bb3 | -11.5812 | -44.6554 | 2025-06-30 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 5db041ba-ade3-3cee-9ff8-ab3ec9fa739e | -7.6362 | -44.6754 | 2025-06-30 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 3670738e-2ca8-3917-9de8-12aedc26115a | -12.9198 | -48.0686 | 2025-06-30 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 2778a0f1-a77b-3f44-b8c3-078b1fe3ca8b | -11.546 | -47.8772 | 2025-06-30 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 0eafc92c-7a66-3096-bf55-6e6c811d273f | -10.8757 | -53.7819 | 2025-06-30 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d950ec65-fb36-3a8c-b1ce-8e6a7769ca10 | -7.6364 | -44.6524 | 2025-06-30 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 192.9 |
| 31fba2cb-d9b4-30bd-9632-728bf6800113 | -11.5779 | -44.8413 | 2025-06-30 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 6cc3ac88-14b2-3e1c-8a22-f7c16928b2a0 | -7.7133 | -47.8453 | 2025-06-30 13:50:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b8787f5a-2fa2-360a-8164-f62bb0194b87 | -14.2247 | -45.5036 | 2025-06-30 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 3527ab5e-eecc-3a0a-910b-ccc3b272e0db | -14.2052 | -45.507 | 2025-06-30 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| c0342ee5-8da0-3e1f-8054-7051ea3accbf | -14.2242 | -45.5269 | 2025-06-30 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d728e690-0925-3258-a8ef-b8c5b64aa6b9 | -7.6362 | -44.6754 | 2025-06-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 422cc58f-8595-382c-b032-b2cfd0206b44 | -7.7133 | -47.8453 | 2025-06-30 14:00:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d042f723-7a6a-3d86-9cbd-bd5b8d63f26c | -11.546 | -47.8772 | 2025-06-30 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 9e557cfa-ed3b-3310-b1e6-f726bebda66c | -14.2052 | -45.507 | 2025-06-30 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 6296d178-50d7-3dad-b405-14f5802cca68 | -11.5779 | -44.8413 | 2025-06-30 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 0a3899f9-cdfa-3f99-b3c5-7ee8b6fbb897 | -14.2247 | -45.5036 | 2025-06-30 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 2170c0ac-10aa-315e-a526-5bd1785178e0 | -7.6364 | -44.6524 | 2025-06-30 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 51b24d48-79f9-35d8-b614-a0f0f8e5de22 | -10.876 | -53.7614 | 2025-06-30 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 45e025d5-afea-34e0-a122-2dcd631ca971 | -14.2242 | -45.5269 | 2025-06-30 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| bda8237d-3d01-345d-87d7-f4a95dff8b31 | -11.6004 | -44.6525 | 2025-06-30 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7e48af59-3494-34a6-9836-ff73450d7f7a | -10.8571 | -53.7631 | 2025-06-30 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 7499fe76-0ae5-3a96-aa87-85c8895b4880 | -14.2052 | -45.507 | 2025-06-30 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |
| d7381f36-5db3-3332-a500-823a9f11b731 | -10.8573 | -53.7425 | 2025-06-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 32bb68ba-7cdc-3654-b4e2-17b2b5b3d2d5 | -7.6364 | -44.6524 | 2025-06-30 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 9fe61761-fc2b-3579-959e-288c5c6490a8 | -14.2242 | -45.5269 | 2025-06-30 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4191f83a-4459-314d-b1cc-a307a9f8926f | -11.6004 | -44.6525 | 2025-06-30 14:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2861afa6-b95d-3528-914e-f18e6574e8c3 | -14.2247 | -45.5036 | 2025-06-30 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| e8d4fdc5-8430-37c8-90e2-5b0ba08ecdf5 | -7.7133 | -47.8453 | 2025-06-30 14:10:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 286d5738-0e09-3e98-8c13-3331e0b44c1e | -10.876 | -53.7614 | 2025-06-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| cfe400e8-be13-37ad-98a0-6bb61cf1948b | -10.8757 | -53.7819 | 2025-06-30 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 9b16e2d2-8a98-3cf0-b900-7702d7af5a64 | -11.546 | -47.8772 | 2025-06-30 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 160.3 |
| a308d094-677f-37df-b0c2-570613f9201c | -10.876 | -53.7614 | 2025-06-30 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| ab0fe078-92a2-339d-84eb-7bd180b6f6eb | -8.5722 | -51.5761 | 2025-06-30 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 1bad22bb-f696-3e37-8daa-74732d7dcc3a | -10.883 | -56.4567 | 2025-06-30 14:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 75c18de4-507d-31d4-a941-da0e8bc7ddf0 | -13.4901 | -52.9715 | 2025-06-30 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 001a7ace-1a07-3ed5-b36d-ff7ffd118cb8 | -14.2052 | -45.507 | 2025-06-30 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 5ef2d463-d2fd-3f5d-8a7f-e617637ac558 | -14.2247 | -45.5036 | 2025-06-30 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 74742e43-4851-39ee-92b6-2914111351bf | -11.6004 | -44.6525 | 2025-06-30 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 112a5169-c557-33b4-ae3f-3da76ea5c7b1 | -10.8568 | -53.7836 | 2025-06-30 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 4e985452-dda9-3318-a89f-f43bbdadfe7e | -11.546 | -47.8772 | 2025-06-30 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| d9615c0e-41cb-336c-84bc-33c6a8284034 | -7.7133 | -47.8453 | 2025-06-30 14:20:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| b3690b88-f010-37e5-9750-1586c46bc626 | -12.9198 | -48.0686 | 2025-06-30 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 906e564c-81f4-3608-8372-dae12be60362 | -10.8573 | -53.7425 | 2025-06-30 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| e0a8e93d-b693-375a-92f7-475c64e9cdb8 | -11.6004 | -44.6525 | 2025-06-30 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2790b8fe-d1d7-3b4e-81af-3149622b419a | -11.546 | -47.8772 | 2025-06-30 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| c679ff47-c2e0-30cc-9d90-6ffb438804bf | -10.8573 | -53.7425 | 2025-06-30 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 262137fe-5cd0-3b08-bdda-a0d285b689e2 | -10.8571 | -53.7631 | 2025-06-30 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| d575ee3f-3e77-3821-90dc-96b71094c62f | -7.2586 | -43.1586 | 2025-06-30 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| 2913203d-fe44-3f2b-abd4-fc4716f43fa2 | -10.876 | -53.7614 | 2025-06-30 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| ea813a40-7473-3621-b011-c57ffd37f847 | -8.5722 | -51.5761 | 2025-06-30 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 7f540db3-12bb-3159-9a9a-aee67d808d99 | -11.5719 | -47.4521 | 2025-06-30 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| cdb7880c-2341-3bc5-b895-54f4deee5ed5 | -7.7133 | -47.8453 | 2025-06-30 14:30:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d934759b-3cce-34ab-b8c7-31eec3107de6 | -10.8757 | -53.7819 | 2025-06-30 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 6c62c4dc-cf6f-32ae-9f16-1cc5a297bfc7 | -14.2052 | -45.507 | 2025-06-30 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 185.2 |
| c6059afb-fc8f-3071-a7cf-7c1e9e2194bf | -7.6364 | -44.6524 | 2025-06-30 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 449c0abc-36b7-3d14-a327-aa3e1ea415fb | -10.8571 | -53.7631 | 2025-06-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 7355249e-cec5-39ae-8ec7-5f4aadabb855 | -7.6364 | -44.6524 | 2025-06-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 249.2 |
| a8bf4020-73f2-32b3-8562-8024eed656bb | -10.8757 | -53.7819 | 2025-06-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 0d14c218-6278-39cb-8492-51b05bc2dd17 | -10.8573 | -53.7425 | 2025-06-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.3 |
| df785056-d2e2-3b34-9efe-16075a2b3803 | -10.8762 | -53.7408 | 2025-06-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 798a00c6-88ce-38b0-919b-afbcb917de8f | -11.5719 | -47.4521 | 2025-06-30 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 8cd3134f-9345-3a2e-9cc5-8d45893d7fe9 | -7.6362 | -44.6754 | 2025-06-30 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 86dd8575-ffad-3e73-82d2-32fc3bc81e5e | -11.546 | -47.8772 | 2025-06-30 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| d879874f-0259-3f12-9775-44beb2d34ea0 | -7.7133 | -47.8453 | 2025-06-30 14:40:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 72d09be8-598c-36d0-b93c-f2ca0845c65d | -14.2052 | -45.507 | 2025-06-30 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 5e505636-abb1-38ff-9dd2-cb5e9969c11b | -10.876 | -53.7614 | 2025-06-30 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.6 |


