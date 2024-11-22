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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d3c8123-3654-37c8-8140-e76e90130a0b | -3.2384 | -54.2632 | 2024-11-22 04:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| bdf08833-e21a-31d4-a8c8-2d1d8025a0a4 | -3.4593 | -45.8881 | 2024-11-22 04:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| bc47a26b-60e7-34c1-ad4b-65e67be3b05b | -3.2201 | -54.2436 | 2024-11-22 04:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 754c2439-b82f-36cd-b0f2-d58e5aa7e9ab | -3.4976 | -53.7935 | 2024-11-22 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 7307ed4e-4009-3b1e-ba4d-c1883ace527f | -3.22 | -54.2636 | 2024-11-22 04:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0d2f9d32-5617-3783-a13a-9f0741f8a296 | -3.4975 | -53.8137 | 2024-11-22 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 0004ecb2-b9ce-385c-9e63-39a9d7e0de35 | -3.2768 | -53.8199 | 2024-11-22 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 8c26045e-916e-325e-a8af-3bf3b3b6ddf8 | -3.23 | -54.25 | 2024-11-22 04:00:00 | MSG-03 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c521e241-5555-390e-b5fb-541e5c25dab0 | -3.2951 | -53.8395 | 2024-11-22 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 2534f5fd-f1ef-3774-92a2-a5bdce2f4341 | -3.2385 | -54.2431 | 2024-11-22 04:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 210.7 |
| c68f2ee7-0fa2-3132-939c-f01f39e7375c | -3.2384 | -54.2632 | 2024-11-22 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 094ef3df-4e2f-3a00-8472-11f68404e0ca | -1.1287 | -53.3951 | 2024-11-22 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 64d9dd61-bf4f-321e-aa63-c7ca6ddeb27e | -3.22 | -54.2636 | 2024-11-22 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 499b0f63-d200-3610-9181-9e0d9a66a66f | -3.2768 | -53.8199 | 2024-11-22 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 3ea7c680-46ac-3483-b03d-c488d5716cf0 | -3.516 | -53.793 | 2024-11-22 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| dda7278b-61b6-3fbf-89c9-b568ee562362 | -1.1857 | -51.948 | 2024-11-22 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 18a040ed-80be-31ca-9735-ed3a8a40fe77 | -3.8355 | -52.2576 | 2024-11-22 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6ab29550-50f7-3d9a-84df-d537f9581cc0 | -4.0131 | -49.9207 | 2024-11-22 04:10:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7d547d09-675d-3002-b3c3-d6de79164c6e | -3.2386 | -54.223 | 2024-11-22 04:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| d98d6cf4-35d8-38cf-9dc2-4a59d52f0d4f | -1.2041 | -51.9683 | 2024-11-22 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 041e3ec4-c364-3eea-96fc-4a26fae3e3d2 | -3.2569 | -54.2426 | 2024-11-22 04:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| bdd25047-82df-31ea-a9da-a47a5f47e4f4 | -3.5159 | -53.8132 | 2024-11-22 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| f7867eb1-a921-307b-a66b-57d6ed37d3bf | -3.2201 | -54.2436 | 2024-11-22 04:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 4afe6fd6-fa0b-3952-9185-bb9e1e150e97 | -1.2041 | -51.9478 | 2024-11-22 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 7c284d46-cff0-34f6-a7d8-f2cc7780b69c | -3.4592 | -45.9104 | 2024-11-22 04:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 1985e8e6-0cac-3c39-a383-76dfe0ade5df | -3.2767 | -53.84 | 2024-11-22 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| f842a18b-b700-3ca0-853e-a3b6adb8ffdb | 0.46879 | -51.3403 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a509115a-3f86-3334-9003-7b45e0d24109 | 0.43233 | -50.78238 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4e920307-94b1-3a9f-8915-5778b2a99a69 | 0.43179 | -50.77888 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d55f4d9-5a49-39a4-8905-258039b51fa9 | 0.43126 | -50.77539 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56b1f3a0-79c8-3f7c-a306-9f097380dc64 | 0.43625 | -50.77815 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8b2e7587-f89f-3e76-bb6b-a59a28cf11f3 | 0.43136 | -50.78251 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b754d83a-1d05-3bc9-aef5-1dd44097d419 | 2.37436 | -50.77214 | 2024-11-22 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e20cee3c-d6b3-3aab-8325-0237e66eb7f1 | 0.43192 | -50.786 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6906f45-0ba5-34bd-a2cc-7939d861e003 | 2.37884 | -50.76373 | 2024-11-22 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62f42fbd-e9a3-3782-8d12-0677c2bd0771 | 0.43724 | -50.77799 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 65206e29-c71d-3a41-be38-573f5008a56a | 0.46313 | -51.34118 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a50d16fb-1578-3132-861a-69fa1d5cbb9f | 2.34018 | -51.64713 | 2024-11-22 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d60e56d8-f826-386e-8489-7bf3015ac6e1 | 2.37492 | -50.77589 | 2024-11-22 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed412b0c-f968-3d22-ae34-f7f10247b794 | 0.4308 | -50.77903 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 23ab76cb-0ca3-37c7-b502-1f8422e3871e | 0.43569 | -50.77467 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1dc077e-1dd0-30fa-889c-e1e975d6005b | 0.43024 | -50.77554 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ede63fe-a986-3843-92bf-e8ecfca10ec0 | 0.46939 | -51.34412 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edd220ce-09e4-3692-90c8-dcfc48086cc0 | 2.38445 | -50.76288 | 2024-11-22 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6bc06cc-5fb6-3fe6-8aed-908374f81e86 | 0.4367 | -50.7745 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6edafd48-7479-3f82-bed2-d1eab0ff6cee | 0.44215 | -50.77362 | 2024-11-22 04:10:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8eb33c21-0c4d-3e36-b53c-598784ac9eb8 | 0.04054 | -49.46116 | 2024-11-22 04:10:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd6f657c-606f-36ad-aae2-af39715b4ada | 2.37941 | -50.76752 | 2024-11-22 04:10:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74983b77-8928-3d94-bebb-02d65589004d | -2.01485 | -46.95799 | 2024-11-22 04:12:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93c64a8c-129e-32d0-b4cd-c483c2d7dc61 | -0.93687 | -51.71804 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dad85f1-bfbc-382e-8b2f-dd5a972eecac | -3.46899 | -45.91088 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9f7a8ca-7316-3e53-a73b-40d5a4cd9338 | -1.11787 | -53.40625 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 076275f2-53fe-3cab-88da-435679b086ed | -4.0959 | -46.20969 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb0ba0c2-c32d-31b1-ab50-e489041d64c8 | -1.61658 | -52.61042 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1700c1f3-79a0-3666-bdd5-b9c82b9353e6 | -3.88893 | -46.65909 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cda9b89b-8133-32c2-bfd4-6ac1d878a668 | -6.27123 | -44.5442 | 2024-11-22 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9ed70efc-d129-3fe6-be26-f1d946f0a172 | -1.23929 | -51.74535 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9edee39-c8ac-35c6-980d-de68f448dd2f | -4.01928 | -43.98997 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e65311bb-fca8-3d2a-9573-1845a5970bc0 | -2.69872 | -51.86465 | 2024-11-22 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3aa0b9ef-f522-3335-bc99-2bddaa4da077 | -3.85457 | -52.35385 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1a8adb6-9fbb-3f69-bef2-54134ac0de52 | -5.24623 | -42.6396 | 2024-11-22 04:12:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1fba3ea2-80cc-386b-ad24-325e96d1e063 | -1.63275 | -52.66234 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58bd6140-7788-366c-a2bd-932306504f09 | -3.57979 | -54.68564 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4862d46-7938-3647-b9f4-538db9f12c34 | -1.64287 | -52.61764 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46c9009b-68f7-3d2a-8039-7b4b687bcf7c | -2.4279 | -46.51511 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ad89ec1-e2f3-391d-8c00-9509c04835a6 | -5.95246 | -48.0548 | 2024-11-22 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 521cbc57-6cfc-32f5-91b6-2b9b9807184c | -2.63674 | -46.23191 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22e6d686-63f4-39e7-9d8a-b46d4ec7d97e | -5.94865 | -44.46355 | 2024-11-22 04:12:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b36f737-afdf-3020-8f51-0a8a93f93711 | -3.09781 | -53.21565 | 2024-11-22 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1450ddd-aeff-3e2b-af17-89814261751e | -2.35534 | -48.5611 | 2024-11-22 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fb2c0f6-61fc-364e-8ae4-7c7437c49192 | -5.82008 | -44.74583 | 2024-11-22 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 30b01a40-12d8-3d53-a680-3ab869f0446e | -2.78304 | -51.72374 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e57c4513-5439-3c61-8524-5621b13781db | -1.13763 | -53.4042 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e3c1feb-9382-35d3-995c-9812033a57c3 | -3.4727 | -45.91149 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 228c5b54-49c4-3e1b-990c-6aa23d8d3c76 | -1.60098 | -53.21205 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 887346cf-3517-332e-9f9c-2f39dc087445 | -3.75512 | -46.11728 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02167aaf-5a85-3ade-8e7e-fa3f807769d3 | -3.1842 | -54.31964 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eeaeef4b-5e53-3106-a028-a9a560ec9d9e | -1.1124 | -53.40013 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20d8184e-3eec-3eb6-8673-f784cddc1fdb | -0.26662 | -51.56219 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27ef8d5d-3373-3c0e-910e-3bcbefd0c734 | -1.13989 | -51.67816 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fd87d86-f2cb-30d4-9ecd-d56771f4e9fc | -3.10331 | -53.73917 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c435fbc0-4466-3066-8692-3b52ee4ef0fa | -2.69687 | -46.26341 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0d06a58-a693-341c-90f9-1c2d6ae81c2a | -3.10522 | -53.99793 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da5f6375-6efe-3a58-8fda-8e533bd144ee | -2.68762 | -46.17562 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05d17817-97f6-3af1-9dc1-5be4f2c173f7 | -1.91504 | -46.44257 | 2024-11-22 04:12:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3baabd6-9ba0-371e-ba3c-1e484e5f1d33 | -3.51129 | -54.69007 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79c18bbc-00b6-318a-a978-1d55dcc54f8a | -5.14963 | -45.8167 | 2024-11-22 04:12:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e2a1cf4-1fe9-3372-a744-3760166651f7 | -2.71017 | -54.13858 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d60de11-401a-3660-b159-fd38c9a7bf85 | -3.26869 | -53.82943 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1955f46-2875-323b-80e2-edca416d43b6 | -5.00448 | -44.79568 | 2024-11-22 04:12:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b02695f8-418a-3338-acfa-c7f7f2d4ad5c | -4.73315 | -45.71531 | 2024-11-22 04:12:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5fc8b6f-4a38-30b1-8ae1-deff7c9b7b39 | -2.69328 | -46.85036 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ced390c7-0602-3f9b-8268-ec0f8f53443e | -3.75929 | -46.12051 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 31eeb306-5155-303a-8882-10b96997a09b | -3.27417 | -53.83511 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02a94ecb-4213-375d-8268-7804d87d7eae | -5.63033 | -44.5336 | 2024-11-22 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8afbd0c2-a5a8-3fa2-81ce-6496f530bc0b | -5.93185 | -43.78215 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 036f3261-5683-3e3b-b6d2-712b722b4ada | -3.10699 | -53.98733 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 809256b4-37ff-347f-b02e-22d67b715a8f | -4.40166 | -43.71825 | 2024-11-22 04:12:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d13e7e17-bef1-3cf4-8f8b-aa80ed86a405 | -0.30427 | -51.54469 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c774adb-3636-3bd9-90b8-2cceee3e76d7 | -1.18879 | -51.95317 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README18.md)
