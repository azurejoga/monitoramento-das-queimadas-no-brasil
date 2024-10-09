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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49e6aa30-583d-3224-a60d-e0f88002f3aa | -19.80017 | -45.60977 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 13beb12f-a81f-3d60-b7ac-d704a2df5863 | -19.79963 | -45.61449 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| afbaafcf-c0f7-39cb-a163-1957a5872361 | -19.79909 | -45.61911 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c425aeba-917d-344a-bc81-6b74d3a2516d | -19.79855 | -45.62376 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fe5e1e5b-6fa2-3000-b4d7-30678fc66744 | -19.79624 | -45.60447 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e183d56e-f8bc-3967-aab1-30f9638f8ee3 | -19.79569 | -45.60923 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 77c8865c-ac54-35be-8416-0d665bcf82d2 | -19.79515 | -45.61393 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5c7ee4a0-a800-3bfd-ba5c-78f0934d6f49 | -19.79461 | -45.6185 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f7a1c894-822f-3e81-a624-dc41a9e5c854 | -19.79344 | -45.60714 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e63b890-0313-302b-b2f9-4f9bda4c10a9 | -19.79286 | -45.61185 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83fc70a1-0396-3d3c-97b0-51ab5a4fa280 | -19.79229 | -45.61646 | 2024-10-09 04:42:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ab8d554-6b1e-318d-a8a4-d3752397db75 | -20.81628 | -45.63024 | 2024-10-09 04:42:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb0fb5b6-da79-3b8b-8fb9-119fe243fbfa | -20.81174 | -45.62971 | 2024-10-09 04:42:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21085eb4-a02a-335e-bfa2-e5b358d849ed | -20.80721 | -45.62912 | 2024-10-09 04:42:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cb80651-3260-3660-a60b-a1ad4c24f7fe | -20.80666 | -45.63388 | 2024-10-09 04:42:00 | NPP-375D | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a54745ff-ae89-3a4f-94a8-9de047fa0b18 | -22.75512 | -47.24329 | 2024-10-09 04:42:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d282e37-0bab-381d-ac43-bd78bd7069ed | -22.75461 | -47.24747 | 2024-10-09 04:42:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c95b3e8a-3e0c-300e-912c-d002ae0e3507 | -22.74744 | -47.12868 | 2024-10-09 04:42:00 | NPP-375D | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5e6b85a9-1ead-3126-a7a0-f87860fb65ba | -22.61176 | -46.98079 | 2024-10-09 04:42:00 | NPP-375D | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de33765e-a288-3d4d-abff-e5b3fdea885a | -22.282 | -46.80904 | 2024-10-09 04:42:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef73fca3-22e4-3d59-82f8-6480680d58a3 | -22.28146 | -46.81351 | 2024-10-09 04:42:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12b0a4c1-dfe3-3e3e-b695-c15bc2583ce5 | -22.27773 | -46.80829 | 2024-10-09 04:42:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fae47f5e-5e02-3761-acc4-b1f78e60c75a | -22.05864 | -46.88916 | 2024-10-09 04:42:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62f2696d-90cb-3a58-97fd-2c87f2ca3f69 | -22.05814 | -46.8933 | 2024-10-09 04:42:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c38074ab-1fc1-362b-b89a-7cd08b1fb225 | -22.05439 | -46.88865 | 2024-10-09 04:42:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afc22b8a-be04-3566-834f-e917300d8ac1 | -21.58159 | -46.97985 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e2e3133-7f46-3aee-b08d-ed777e533ddc | -21.58113 | -46.98372 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2da1e18b-ca6f-3846-83f5-550853b5f337 | -21.57786 | -46.97542 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 57af03c9-436a-32e0-9685-492064b70f84 | -21.57738 | -46.9794 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c456f0e1-3d83-361a-86e6-c36a07cd82c9 | -21.57692 | -46.98323 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 84ca548d-799c-3627-bf35-c23553a7652d | -21.57319 | -46.97877 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 81ceb756-283d-3ef1-b7b7-d7a80723b29f | -21.57272 | -46.98265 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bb295b9a-835f-3e18-ac87-2896d37e0f4e | -21.57226 | -46.98651 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 77037b0a-8f01-3cf2-9349-d41fb8ea2907 | -21.569 | -46.9781 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 409e46f2-bb30-3672-b019-516e1c21cdd2 | -21.56853 | -46.98207 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 06d34944-715f-3bbe-b261-ed1ba396ab91 | -21.56806 | -46.986 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7340f825-c60f-3d69-b889-7bb5e7e870ff | -21.56531 | -46.9733 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 349bf8b2-8d95-315f-ad76-3827d88c2193 | -21.56482 | -46.9774 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d24bbe0a-94b2-38d6-b2c4-7b7a6f7f2b84 | -21.56434 | -46.98145 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 95fa7fae-5e7b-3877-b603-1dfb16b2ea29 | -21.56385 | -46.98551 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 416c79b1-0a05-31fc-8b8b-d30b99ba457a | -21.56112 | -46.97267 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d92bedb3-2d81-3428-a63e-2be192251347 | -21.56063 | -46.9768 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a633e960-ee16-32ca-b188-2febc726bf27 | -21.56014 | -46.98092 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| de72280d-e2ff-3ee8-8cda-ec37e41efb3a | -21.55965 | -46.98497 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 880c38cf-c3bd-3bd6-ab32-4035222d8bf3 | -21.55691 | -46.97216 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f875caa1-4523-3d94-8322-7da2f9ff5abf | -21.55642 | -46.97634 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 651e12b6-dc6a-3d23-b32f-fa91c0c0dbcf | -21.55172 | -46.97997 | 2024-10-09 04:42:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae8475ce-2eb5-3b3f-81c3-709b03b90884 | -21.63973 | -47.70948 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac48daad-ebba-384e-aa72-d0ae28ed5f08 | -21.63903 | -47.715 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e845ed1a-6d67-3076-9431-9489cba2544f | -21.63572 | -47.70892 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2cbedbf-d34a-38ea-bb65-d260e1474022 | -21.63239 | -47.70291 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24d0b781-dc29-3a60-887b-31cb5843d452 | -21.6317 | -47.70836 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b2ce372-a21a-3528-9425-765e5874f3e7 | -21.62838 | -47.70235 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35a0a27b-be58-3cbf-a297-e4fed9ae9fc9 | -21.62769 | -47.70781 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d049d62-07a4-3fbd-b931-46e8b0686ed5 | -21.62436 | -47.70176 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93709606-8acd-3e35-87d9-94bbda46d6d5 | -21.62367 | -47.70724 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e59eccb9-ca43-3a15-aad7-e0b6e0559983 | -21.61897 | -47.71207 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3541d2de-fe29-308c-9aed-ee4b021ce6cf | -21.6183 | -47.71743 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 283fa65a-8e1e-3655-80f1-67e49fe8ede7 | -21.61762 | -47.72282 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e73c8003-726f-3258-a935-59be190eb809 | -21.61516 | -47.67738 | 2024-10-09 04:42:00 | NPP-375D | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b23d78c4-30aa-33da-b379-80eee3071c67 | -21.61429 | -47.71686 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bff1bf4f-3d65-30dc-8f18-cb5cdd6daad5 | -21.61361 | -47.72224 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e5a8ffab-9e4d-34ca-80d1-03c12eed291a | -21.61183 | -47.67125 | 2024-10-09 04:42:00 | NPP-375D | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba6de630-3141-3fef-9253-a5f24dc70ec9 | -21.61114 | -47.67682 | 2024-10-09 04:42:00 | NPP-375D | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f515f76-5990-3004-8e2b-6e38fa4573ce | -21.60959 | -47.7217 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f1e1e3d-7062-34b9-baff-4fc2e6150578 | -21.60781 | -47.67065 | 2024-10-09 04:42:00 | NPP-375D | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1eff7fb0-3751-3a1f-86cc-60c4b8a167f3 | -21.60711 | -47.67626 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dbd7facf-41fa-3a4b-b6f4-afecab349465 | -21.60641 | -47.68193 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 659b5902-0dc3-34ef-8fa4-1ab610f8021a | -21.6057 | -47.68761 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 319d26f5-285c-3bd3-9c78-ef9a4db24d83 | -21.60558 | -47.72117 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e9d8249-6aae-3d1f-9c8f-a2981a90b4ea | -21.60499 | -47.69327 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d2736ef-c4fa-3c49-aea3-c0830a8fc583 | -21.60429 | -47.69885 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 055f0259-c578-35fe-a66e-bc6e56f4290c | -21.6036 | -47.70436 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67ceb9fd-df48-3d2e-9a04-c409751bb510 | -21.60293 | -47.70973 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c2ccbf9-61a9-3afb-a4fe-569791edfdfd | -21.60098 | -47.69264 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8486f6a-8610-36e5-8434-af9db0ffc6a3 | -21.59958 | -47.70382 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2f00d96-73ff-31f8-b86f-76a99398f97d | -21.59697 | -47.692 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 94ec97db-f708-35ff-9d83-7643c2cf28e2 | -21.59557 | -47.70326 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 84f60b75-680d-3bc7-95f4-3f6afd4c81e6 | -21.59415 | -47.71466 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5dc57e6-05b2-3574-a39c-a9f8666708b0 | -21.59345 | -47.72028 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4788bb9-ad4c-3ea9-92d5-8b68e4b72c66 | -21.59083 | -47.70853 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17af41f1-446d-3cc2-b2d8-c7a7ea3d10cc | -21.58757 | -47.89612 | 2024-10-09 04:42:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62229a02-0bbd-3c30-bcd2-f18c64c0d90c | -21.58727 | -47.96184 | 2024-10-09 04:42:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19261297-ab14-38f3-af3e-38802cf22759 | -21.58332 | -47.96127 | 2024-10-09 04:42:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 093c6dbe-f55e-3e74-9f43-99bfa0d47583 | -21.58223 | -47.90635 | 2024-10-09 04:42:00 | NPP-375D | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7bedb91-f155-30f0-bf24-a5adbba662d7 | -21.58168 | -47.87873 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 461885f5-baed-3f43-a9b3-27ff727cbc3b | -21.581 | -47.88414 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a98ea813-9c68-3825-9818-824eb12dc2d0 | -21.58032 | -47.88956 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36451a9d-7650-33d6-9a80-d44accfacc65 | -21.57963 | -47.89496 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 212898ce-9bcb-36a5-86e4-c6992285a431 | -21.57895 | -47.90037 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2f3e00d-00fa-3c98-af4c-1103cd3567b2 | -21.57827 | -47.90577 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c2bce5e-0711-3c05-9a33-5f0359307d98 | -21.57771 | -47.87817 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c9f69377-f882-3eec-a5c2-d7bcd4f46db4 | -21.57703 | -47.88358 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 26ccf437-6da9-3c30-bed5-0b088f1f27da | -21.57635 | -47.88899 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b44b832d-4f34-3250-b90c-541027fabbe4 | -21.57566 | -47.8944 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 857a5d9d-3b00-3ada-a50f-d2941f26e48c | -21.57498 | -47.89981 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b310208-db47-3613-bb05-13448547a3aa | -21.5743 | -47.90522 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76597329-89f6-3e09-89b5-f168319ee288 | -21.57306 | -47.88305 | 2024-10-09 04:42:00 | NPP-375D | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bac1c38-a2e0-3748-8998-3c44f948772a | -21.40477 | -47.80679 | 2024-10-09 04:42:00 | NPP-375D | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4acb4c68-82fe-3f28-9daa-6edd37c869d7 | -21.31896 | -47.60946 | 2024-10-09 04:42:00 | NPP-375D | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README153.md)
