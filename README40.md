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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a55aad0c-8723-3df1-bbae-00615c9c9e8f | -2.24903 | -46.73853 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9189d49-4b9a-3e70-afbc-33f748cb0678 | -2.24898 | -46.76077 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ac3279a-6556-3dfd-8ce1-174eb48e164b | -2.24845 | -46.74214 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e13ad0a-c0d7-3434-8d81-7edd3a95a0fb | -2.24841 | -46.76439 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02794db3-bb0f-38ca-b4d0-9c1d7d5bcd17 | -2.24788 | -46.74576 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 114a897a-d627-31cd-8a9e-36177a135e69 | -2.24616 | -46.75663 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92254249-ee99-35d6-a7da-9efb0ee5af2d | -2.23989 | -46.77419 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2a2183e-5fce-3339-b111-031c43555328 | -2.23889 | -46.71474 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40866708-b57e-36b0-9f43-2bc2c1ae31da | -2.2365 | -46.77367 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c073e330-887e-3d9c-8809-d52385103300 | -2.2297 | -46.77261 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ee456ed-3ebe-318e-b684-7baa860bf4f5 | -2.2263 | -46.77208 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42c106a3-b345-3d85-a677-9efac9c0f119 | -2.19504 | -46.72692 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eedec39b-97e5-391a-b051-e9e85046cb63 | -2.19391 | -46.73415 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b203d850-4f60-3c94-ac61-8f8f8eb339ec | -2.19334 | -46.73777 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25194755-9cf1-3b54-bbe9-63ba9a7b0aed | -2.19277 | -46.74139 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cc0af11-d9b2-30b9-8bcb-829a10a55f76 | -2.1922 | -46.74502 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f184e81c-1496-32d5-9f9d-0308799358f5 | -3.36135 | -46.48722 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1288e1cc-16c6-3bf3-9a63-deb88f963014 | -3.35799 | -46.48672 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79f1ad5e-838f-3864-ae79-e0eb17cd66d8 | -2.77934 | -47.28961 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6bdb008-5d37-3913-bc02-454b107796e3 | -2.58168 | -47.06242 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36201ab9-06ea-3211-85e2-03bb649be947 | -2.5788 | -47.06249 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf66f845-d4c4-36c8-99a3-f308dbd0ce51 | -2.57826 | -47.06186 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88b226b3-596d-33b9-a9d5-f2ee16f11351 | -2.57538 | -47.06194 | 2024-10-15 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31e60c3a-7ec4-3f51-a72a-92c380a48ad7 | -3.86659 | -46.45791 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29fc5ee6-1233-3f74-af6a-a792194101dd | -3.86604 | -46.4614 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 223103fe-7c22-3bde-a005-e007a45740c8 | -3.86386 | -46.46114 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d4beb43-047a-3e94-b9d1-c1bd619d00ad | -3.86275 | -46.46818 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37f315ce-369f-3615-bf85-7b71661c4314 | -3.86164 | -46.47526 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe96a93c-c9f2-3ea5-a5fe-c402eb3a0338 | -3.8594 | -46.91441 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a61173f1-489e-373d-a855-99f382dcde5f | -3.85883 | -46.918 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5d0355c-9644-3e47-9130-6496dc8200fe | -3.85716 | -46.90668 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca552a1c-1ef8-38c7-9284-32b1df6054b9 | -3.8566 | -46.91025 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78580bad-a64c-3a01-851a-7f4f4763238c | -3.85603 | -46.91383 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33fd60da-c00c-3eab-bfd6-1944fb20b3b9 | -3.85546 | -46.91743 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d9978ff-95ce-3c1f-9c00-c24b526fb73c | -3.85489 | -46.92104 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f8de12f-7bc0-3fe7-9a68-634c0357f0b6 | -3.85436 | -46.90255 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fc4caaa-e76c-3b0f-b5dd-2cf88417169a | -3.85379 | -46.90611 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4189d0a-cc17-31de-8799-ea5c3c39646a | -3.85323 | -46.90968 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b6c4a78-a9c9-3e63-be05-4240533ff3a5 | -3.85098 | -46.90201 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6250b50d-9fc6-316d-872f-a9c3420d87c7 | -3.85094 | -46.9241 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8af7160-b89b-351c-b1a0-a4ffd2ae6386 | -3.85042 | -46.90557 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6c0f9b8-07b3-3ffa-9bb3-6ac22d6e01ab | -3.84985 | -46.90915 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b910884-da2f-30d9-9ed8-5d6655e6c9de | -3.84928 | -46.91274 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a03c555d-026a-3588-bd43-ef4b806a8ca5 | -3.84817 | -46.89792 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ae9dcc9-b11e-32aa-b75e-77b65144b26f | -3.84761 | -46.90148 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dda49f01-6a9f-31b1-9e1a-c1331d58f2dc | -3.84756 | -46.92355 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf1a97e3-770e-3624-b2e0-69db91a1a1c7 | -3.84704 | -46.90504 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28165db4-678e-3c7f-8bc1-c0843f49ff3c | -3.84647 | -46.90862 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b35aaefe-f4ff-37b4-ac2f-c4b705fbe188 | -3.8459 | -46.9122 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dba8c8b6-bcd2-341a-90b9-0eea1b0a5223 | -3.84491 | -46.47258 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 019e52d5-e4d9-3414-98fc-469edc5a5a1d | -3.84476 | -46.9194 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4508a17a-3876-35e2-ac20-603c6fd1a3c6 | -3.84436 | -46.47612 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df80c82c-7270-3e60-afda-d040ba7d8db3 | -3.84423 | -46.90096 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ace71b1-7207-369e-b648-4a37e3f7e1e9 | -3.84419 | -46.923 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 530b10d6-bf66-3d20-acb5-3c00bd49bf9a | -3.84253 | -46.91167 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4f4a245-9272-3ac0-8bf1-b2cd57900d03 | -3.84195 | -46.91526 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7183219c-08d2-3038-a459-5f62fef73b6b | -3.84138 | -46.91886 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9ac97c1-60a5-34a8-9245-a3ad680609d0 | -3.84081 | -46.92246 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b97233ea-dd94-3bb2-8084-0525f50dad45 | -3.84045 | -46.47914 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f94c1dfc-158b-376a-8970-58e0f5684f31 | -3.83915 | -46.91114 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98d4fed5-3d4c-356f-8e88-24e478e54bc1 | -3.83858 | -46.91472 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f68fe82c-2272-3f6b-9c81-550f90f9e0a5 | -3.83822 | -46.47155 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 007fb17a-b8e2-3655-8989-04a4ab8ff2c6 | -3.83801 | -46.91832 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9262c4f-b384-3010-bc43-6e44e7e604f2 | -3.83655 | -46.48212 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 277481a1-0c74-33cf-88de-c2ccb2c59ff2 | -3.83655 | -46.46043 | 2024-10-15 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 003ad448-347e-359f-a196-782e83569ebe | -3.83633 | -46.90706 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e2199f4-8a5a-3c56-bebe-b57bafc13a08 | -3.83577 | -46.91062 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 137be400-a787-3cb8-a7e3-a78fb0d3c5db | -3.83295 | -46.90655 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7491202-1cc9-344d-ab69-efc65cbedad0 | -3.83239 | -46.91011 | 2024-10-15 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a64c8929-da38-3491-bd76-0f4829fd28f6 | -3.82458 | -47.48092 | 2024-10-15 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56a346c3-7d74-37fa-987f-c5a53407a66d | -3.82115 | -47.48037 | 2024-10-15 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02c63d2d-fae7-3e00-81e9-08d074348a89 | -3.80112 | -47.48096 | 2024-10-15 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c47f600e-5d1c-3291-b407-2c9c9b970b7a | -3.7614 | -47.50913 | 2024-10-15 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfa04e96-600a-3d39-9718-c38226781b5e | -3.56219 | -47.35675 | 2024-10-15 04:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b56711d2-0616-38c5-9897-879822be4b60 | -5.00909 | -46.49108 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85572585-0e6a-32af-9e34-5aed20109b90 | -5.00854 | -46.49457 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a898844-eb94-3b87-9085-8866bbfcaddd | -5.0052 | -46.49405 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0de79c97-46c3-3bb2-9787-6bbc89fa8c76 | -5.00242 | -46.49003 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fab2663-a2ae-37af-b6a9-582ccd710bdd | -5.00187 | -46.49352 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 151b9f03-e0ff-3eb5-9087-ab69b27675e1 | -5.00021 | -46.50399 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5465f0f-2bea-384d-a02d-8c67310678bd | -4.99854 | -46.49299 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eba0f702-e999-38aa-a3ba-838cc3a2058f | -4.99132 | -46.49543 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20bcb00c-142e-392f-b76c-1b0d3d0811da | -4.98854 | -46.4914 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e5f999f-3462-31e1-86b3-833904cb83e7 | -4.98798 | -46.49489 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa0a34b9-4f5c-343d-a870-fe16b4544b9c | -4.98465 | -46.49436 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5eb570c1-18c6-3df3-a066-a0875b63c421 | -4.89906 | -46.69567 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af6959ec-6e57-3e68-bc54-af06ba136f1a | -4.89571 | -46.69516 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb2ef7eb-8480-3121-b17d-b5fb1632db81 | -4.88957 | -46.6906 | 2024-10-15 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec26aa90-992b-3767-98bb-ae82920fb0c4 | -4.87009 | -47.10574 | 2024-10-15 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ece5117-3a0d-3e6f-86a6-10065c094947 | -4.86951 | -47.10933 | 2024-10-15 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df8da8e3-75ce-37fb-91af-421cca75433e | -4.86614 | -47.10882 | 2024-10-15 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30373732-212a-36a0-9505-19817b145bcc | -4.72278 | -46.71495 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91f379a8-9caa-3dee-a198-5c4ea0e79ae6 | -4.65325 | -46.81633 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 804a52d4-40de-36b9-9f2c-e9def79b7571 | -4.65269 | -46.81986 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 854062d4-1e2f-3333-ae33-78b58bbd2487 | -4.65045 | -46.81229 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02c57edf-2347-3b50-a1c2-1e908c59acef | -4.64989 | -46.81582 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 261f7324-cbe5-35e5-a840-c6c8621b6fd5 | -4.64653 | -46.81531 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59a45588-0853-3c07-80eb-0d70d3ac7a9c | -4.63305 | -46.90049 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c09f190a-7127-3430-8b4b-10b8fb0ec48f | -4.62968 | -46.89994 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbd44266-9830-377a-98b2-9cabecd0a8a6 | -4.54445 | -46.5614 | 2024-10-15 04:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README41.md)
