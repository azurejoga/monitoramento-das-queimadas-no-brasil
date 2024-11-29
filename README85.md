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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12a3ce02-96ea-3abb-8b24-18cca2fe2160 | -1.14927 | -53.70229 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ead0c94-2eb7-376e-bdec-c2ad60e581b1 | -1.39255 | -53.63657 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d49f8164-a0a7-367f-b2a6-23ddc2655875 | -1.2734 | -53.02444 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28d59786-e752-38c7-bab2-d3106222fcbf | -1.21928 | -53.38378 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5752a72-71cb-31b8-ac89-5963f81f0a88 | -1.04814 | -51.73627 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 801aa1a5-5385-322e-82d0-3460c9e8839a | -1.07234 | -53.64215 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bcdd107-5d1a-35cb-9745-e7b2a4ceff62 | -1.19643 | -51.751 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5ebf487-1a72-3384-8fb2-803242e21eff | -1.61542 | -52.45974 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2fe018b-6a16-394c-aada-c398ac1f7824 | -1.62537 | -52.45643 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 61ff703f-fe40-30b6-b433-865914eff9b9 | -1.3156 | -51.74015 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 21decae9-8de1-3d9f-a33e-995607df394e | 1.21458 | -55.95107 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7c0dd767-a081-34b7-9719-7af6c081b45b | -1.3713 | -53.63368 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b76302a-8f5f-3a7e-98a5-ffe7eae66367 | 1.45505 | -55.9043 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7faad032-af9b-3ff7-a9b4-4d73f03edd58 | -1.15308 | -53.56758 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1fa7991-647a-3477-8d98-fa52ad500a20 | -1.17705 | -53.88839 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da9d12c2-0d94-39dc-b705-e13ac2b6b6dd | -1.16031 | -53.5769 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8393029-8f6d-3f73-98e1-aacbec947481 | -1.59897 | -52.28543 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3090199d-f492-3575-b1f3-2777cde85b22 | 1.29838 | -60.41539 | 2024-11-29 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 552eb64f-c6fc-3d41-a63b-d04a037cfa52 | -0.29923 | -51.74612 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b01efa1c-a83e-3530-8d69-bd63732d57fc | -0.26967 | -51.62405 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 467816f9-f4dd-30ea-9e58-d575e9e96454 | -1.08196 | -53.63566 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84962bda-123c-3d6f-b389-7a4a81fab8e0 | -1.33562 | -51.92429 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e79482d3-70a8-390b-8204-115d903d1867 | 1.31143 | -60.40961 | 2024-11-29 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3861e623-b6d4-37d1-8638-1c1599607b04 | -1.21099 | -53.55403 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c91e077f-036c-39a2-9539-810193608761 | 1.67473 | -50.66582 | 2024-11-29 05:20:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a6ef381b-b211-31da-8ce3-b2f59a075758 | -0.95265 | -51.65194 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eeca19d7-f4f3-3bf1-aeb5-498d347b89df | 1.33304 | -50.67402 | 2024-11-29 05:20:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c02f470b-42aa-33c3-a8af-bdd4a72b2879 | 0.74018 | -50.86816 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38a4fdc7-8baf-30cb-b80b-8e7e1b55e7e9 | -1.59205 | -52.28256 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 441ba8e7-b2b0-329f-87a7-b4c9b86cae2e | 0.98774 | -50.24994 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e6f56f5-cbff-3a6d-8a2b-9287c5730eb9 | -2.06334 | -46.37854 | 2024-11-29 05:20:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faa6d288-6ab1-3532-983d-3a413d4689b8 | 0.03796 | -51.11349 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7070eb0b-26d1-3095-8d23-a57142324fd3 | -1.10168 | -53.40537 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33c73fda-7a5d-3267-9294-06249f698f2e | -0.56484 | -51.70183 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0eba9555-688b-3c95-a36b-259947b6afc8 | -1.52802 | -52.69107 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb8ecb57-42c1-3b97-87a6-4252c858b34b | -1.31641 | -51.73489 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 595a3ae0-067f-3401-bdf2-68227759ccc4 | 1.32806 | -50.67483 | 2024-11-29 05:20:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb10e765-4834-35f6-ba8d-dc324ff53ca0 | -1.14396 | -48.33664 | 2024-11-29 05:20:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e853d179-80a1-3e22-a299-7db7d74a0780 | -1.08226 | -53.637 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 94bedaa5-d5bf-3750-9d3f-cb6de80156ee | -1.59596 | -52.28812 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b3a3797f-74a1-33c1-9429-a2a04f3a95c7 | 0.93918 | -50.73604 | 2024-11-29 05:20:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25921df4-30a2-3ccd-a281-55022cea3aa8 | -1.2035 | -53.71621 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c71b993-bb41-35a8-a686-9323ffc225d6 | -1.18842 | -51.77111 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea3785da-2b53-3f5e-b478-9a7dda0e92cb | -0.99126 | -51.72209 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83bb6277-ccfe-3b06-bab1-8006d9ea4b2a | -1.23243 | -51.80441 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fce58ada-745d-3f64-9637-cd9e7c155b1f | -0.2995 | -51.74351 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8057245a-df23-31db-9eb8-4d926ef51900 | -1.80125 | -48.77301 | 2024-11-29 05:20:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84aa8107-376f-3ac6-bbaa-a8513d179bd3 | -1.52011 | -52.02687 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b48203da-4b10-39ca-a004-8a4bc2a7f45b | 0.97854 | -50.12808 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33628f89-576a-3f7b-b057-9994da50bcea | -1.14081 | -53.70133 | 2024-11-29 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6d92be5-0632-387d-a12a-803f255d20d5 | -1.08134 | -53.63972 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 512eff97-bfd5-3d1c-9b52-d8f7e77b5fcf | 0.97804 | -50.12496 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cdba384c-681f-3b6d-81f4-30a436e1ab3a | -0.27365 | -51.62993 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 855a64c2-3dad-3d0c-a212-54084a9eacc7 | -0.14276 | -60.86702 | 2024-11-29 05:20:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebaec18c-95a3-3a62-b758-f86fa74d4eeb | -2.33371 | -46.86586 | 2024-11-29 05:20:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d79b778e-1b20-3681-b6cf-fac12b6d753b | -0.27762 | -51.63582 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91917060-755e-3b70-b269-814e41dc2d55 | -1.34555 | -51.98679 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab608abf-98e1-3040-823f-a5e39ae7428a | -0.95185 | -51.65722 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1335dfa-6e92-362b-ab3c-b0acd298384e | 1.25803 | -55.91215 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e42b61c-4d6d-3aa9-b28c-015a3f418675 | 1.22626 | -55.94174 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 940426ec-9cf5-384c-99af-5feffcf50c54 | -1.65254 | -52.49444 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0874bf0-9ada-3beb-9d5a-9f90035b3e8a | -1.18361 | -51.77039 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e160a199-592e-3532-969a-e867062ec769 | -1.61224 | -52.29247 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 639a2eea-1e49-3d46-99f6-746e87cf6c29 | 0.33551 | -49.71579 | 2024-11-29 05:20:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f91970fd-e747-3e6f-a7ed-3f47e90323a3 | 1.22757 | -55.94081 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4cbb956-5a16-3666-9967-7592bb014d5e | -1.61614 | -52.45502 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1625f990-4dc4-37f6-b181-5a5d8a79ab00 | -1.25335 | -54.54184 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33e6fcfb-4b14-3b51-a5db-de0b1350941d | -1.19172 | -54.01236 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de2272d3-5c0b-3a89-a1a6-cf205344b123 | -0.23918 | -53.76081 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c583bc2f-b5f8-31fd-93e3-588c58d3364b | -1.09503 | -53.39187 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| af80f78a-3936-3c27-a5f3-6452b90e4c80 | -0.05231 | -50.82781 | 2024-11-29 05:20:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e36c05b-955f-3875-8126-d331ee2eba81 | 1.85266 | -55.79692 | 2024-11-29 05:20:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f85a865-6968-350c-b833-bd1da6a15b27 | -1.10361 | -53.3932 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4f6bec4-b056-3fa2-966e-840a38860039 | -1.55955 | -52.02394 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 391cee81-fdfd-37c8-bb8a-a47c37335783 | -1.09899 | -54.12794 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 660101b8-7bad-3176-a873-51a5b13683cc | -1.06543 | -53.63421 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 446390a2-d82e-3fd6-8347-a6137f57302d | -0.57042 | -51.69744 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59cfc84f-de25-361f-86fb-32bc209c2de6 | -1.08216 | -53.38987 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2f40593-c3a7-3bb2-a63b-76f922bf46d8 | -1.20125 | -51.75175 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11820615-5dab-3ef1-82b5-868bd3f03f07 | -1.57956 | -52.2707 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 18099a58-1ba0-3c62-a285-a2f0db92f79d | -1.25651 | -54.54757 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f516788-fdd0-3fce-b19e-0647998fc10f | -1.1549 | -53.58371 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34ea92bf-a1f6-3378-b717-e1f44c5a548c | -1.41112 | -51.5872 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 141bbf82-deb2-3a38-b150-af630fbf7061 | 3.20183 | -61.02 | 2024-11-29 05:20:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 669601b6-ea16-3b94-b41c-70472435ec17 | -1.07322 | -53.63954 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 821729c5-753b-3fa1-84d7-d401ba23427d | -1.3314 | -51.92237 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5dec037-028b-317c-901c-dbb160554db8 | 1.21521 | -55.95509 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ae1544e-8ce2-3729-8e9c-feaf8b7271dc | -1.10024 | -54.14638 | 2024-11-29 05:20:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6d5949f6-d201-3c4e-bf61-19a71895318b | -1.53311 | -51.62386 | 2024-11-29 05:20:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| aad5e0c6-9c6a-388c-bb95-0c2f5cab9b91 | -1.53615 | -52.66885 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b898ec9a-32ea-3760-9991-06b4b852eb6a | -1.58347 | -52.27627 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e0f317b-ff6f-3f8a-8683-2b573ffc5a55 | 1.22694 | -55.93681 | 2024-11-29 05:20:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7b9f974-7eae-3853-a274-ad3b7e3518a9 | 0.74175 | -50.87262 | 2024-11-29 05:20:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c831240-98a3-3801-8e60-b480b63a430a | -0.99607 | -51.72284 | 2024-11-29 05:20:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24a58e5b-42a8-3859-b6a6-0875a0c66d9e | -1.08281 | -53.38573 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02fdec21-6e82-3078-85fb-00861251dc30 | -1.62457 | -52.36849 | 2024-11-29 05:20:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a94d1a5-f1de-3cab-a1f0-29a7e81eb317 | -1.07787 | -53.38924 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f847f8c-1922-3403-aca7-d00cf290b742 | -1.53687 | -52.66428 | 2024-11-29 05:20:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a23604ab-3f0b-33e8-b25d-3437b4213c30 | 0.59412 | -60.46661 | 2024-11-29 05:20:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1546a988-97a3-305b-8279-798b575cea04 | -0.75115 | -51.79134 | 2024-11-29 05:20:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README86.md)
