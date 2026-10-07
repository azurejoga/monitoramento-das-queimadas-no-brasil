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

## Dados Diários - Página 237

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f767a5fd-9a37-307e-91a9-22a4770794d2 | -1.28452 | -54.55611 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 67d8ddee-5c83-3c0a-a8b6-4ee1a272ea69 | -1.28851 | -54.55639 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2d8e4a47-2c7e-320e-9981-2ad2303cca78 | -3.54828 | -50.09937 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 8fd52d01-bdf7-31f7-814b-bd140e77012a | 1.6485 | -55.79532 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c52756f7-96f4-32c0-87f9-aac00e2d1bd5 | -2.64501 | -54.37758 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10b6dd91-774e-3350-9852-9894346d27b6 | 0.64726 | -51.78909 | 2026-10-07 16:39:00 | NPP-375 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d6784969-6fa1-3fa8-9aaf-e6ea961830fc | -1.46934 | -54.52334 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 0ec63869-43e5-300a-8497-8d691c50bde8 | -3.11421 | -53.77764 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 66322af6-bc03-3b77-bcbd-8c1c63dc5e7c | -3.08863 | -54.26382 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea40e0af-8127-35c9-8763-70ff7f1511dc | 0.72864 | -51.38631 | 2026-10-07 16:39:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 910747c0-f460-3264-8f9b-c558ae4a7450 | -4.00449 | -56.25442 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 25642906-3f0a-3c12-a1bb-b7cc04c4f199 | -3.79109 | -50.74939 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 0d90d91e-2114-3c5b-b56d-55ba193455b6 | -2.00052 | -45.08713 | 2026-10-07 16:39:00 | NPP-375 | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3436cbfa-52eb-3dcb-a709-d100d5201162 | -2.6774 | -46.06264 | 2026-10-07 16:39:00 | NPP-375 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 8810c8e7-8e2c-3b9d-814d-3794a1d0452c | -3.04948 | -53.91947 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f8308431-96f9-3bce-9969-57cfb9bee0d7 | 1.08811 | -50.73581 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 38dfeb02-461a-39f9-84ae-b2335574d894 | -3.99817 | -56.2553 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a1050cf2-2814-3199-9e89-b22fc0d42a71 | -3.09503 | -53.71538 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 812ece23-af82-3dc5-b72d-8fe147c7a814 | -1.54278 | -54.78028 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 633cdcea-dcbb-3938-af7b-c0c40b1a7c17 | -1.76672 | -55.03245 | 2026-10-07 16:39:00 | NPP-375 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3c96230c-3149-3eec-b8d9-f9db259af8b2 | -3.54092 | -54.64489 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b7927e84-a3be-3472-87e9-dd2a322cc927 | -3.00605 | -56.81208 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a8e2503-6e03-37d0-8920-c94eb9006fc2 | -2.88445 | -54.17429 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ad34616-99f1-3f53-930b-ac92d7b65204 | -2.76016 | -54.09035 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7244702e-814f-3e1d-b49c-2178b96856fb | -3.0965 | -53.72507 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 42757854-ced3-32f3-90fc-f80ffbfb6809 | -2.57081 | -56.16299 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 327d12d2-e502-3bb8-b9c2-5d64d96b450e | -1.27127 | -55.86429 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d3c3495c-e385-32a9-a23f-2a3ec6a5c6da | -2.44247 | -56.55007 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 19c11f93-b8e1-3e8c-8fea-cd74e92e8fc6 | -3.27418 | -54.03443 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 30a99ac8-bc71-3a96-bee4-fef58fab40ab | 1.75553 | -55.5879 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a7746f51-07d0-3a38-8edd-1f5e3d0ff6c2 | -2.99935 | -54.11454 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 191ff95e-1d51-374b-87ce-e899996ef14a | -3.06747 | -57.74735 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 0226519b-8d2a-3638-903d-b07af866b01c | 1.19677 | -51.28799 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5be399f2-844c-300f-8326-f78b59208698 | -4.13182 | -54.25438 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 53ea3406-7dee-3b18-9d19-ff2c5e508d2b | -3.13352 | -51.02705 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0948d592-10d1-35e6-b601-1b89fcb4a4fe | -1.2959 | -54.55791 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fefadd18-c217-326e-be7c-9a584f98efc1 | -3.03205 | -57.49148 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1a3dd7c8-88d1-3d1b-b542-77c2c8e301c3 | 1.73248 | -56.0822 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 29a15603-2131-347f-b058-03a4c7f2c789 | -2.88379 | -45.73819 | 2026-10-07 16:39:00 | NPP-375 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 286a4f9c-afff-3f06-b368-e61e35a88038 | 2.45087 | -50.93909 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1b397d2e-288d-37de-888c-0b40483816b2 | -2.78356 | -54.06278 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| a6ce7bab-77c5-34d1-b8bd-4fb5833e0e10 | -3.1428 | -54.36531 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 4a1c4fd1-0fc3-3e41-8620-c0bb71932525 | -3.28562 | -54.07509 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 4e567034-500d-3dde-b505-cd62da9b5116 | -3.85453 | -55.98316 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e48402ce-d930-35b1-95b6-d81cde5a84c1 | -3.10763 | -54.27895 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 8b8f441d-3535-3ec1-8c15-c62f3f324f2e | -2.5032 | -56.13014 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| aebb5dea-3f0c-371b-9142-973f6fc2a5f9 | 1.69636 | -55.64194 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| facc9e39-2db6-3ad9-9649-8114afd8f261 | -2.9637 | -54.21183 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2d28fcf5-de3f-37b7-bde8-494feded8259 | -2.29509 | -45.88765 | 2026-10-07 16:39:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3404c4ef-c417-3477-98b4-4245fc9757b6 | -2.65279 | -56.53793 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2e653740-3d21-3acf-beba-456d6fb3e5a5 | -2.57011 | -56.15835 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 74cbf19a-4095-3f70-82c8-73e97a844369 | -1.29149 | -54.56563 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d590f56e-8ad2-3b8f-821b-963a3b34d186 | -3.30109 | -57.84969 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 79839592-c33a-384e-82ff-ce4b2d4a0ba2 | -1.27658 | -55.85928 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| fae84019-433e-3c96-9ae7-20c27a0aa25a | -3.289 | -54.06033 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3a273ac-277d-399e-9d01-3c7f144b2e0a | -2.77296 | -54.10247 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 7165460f-d09e-34df-893a-bbb012620397 | -2.46931 | -56.06892 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 94dba214-d0ff-3b61-8be2-db3756874be5 | -1.34124 | -55.69019 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c422ca8a-21e4-39de-9bf6-cd124fcfd360 | 0.80539 | -51.22515 | 2026-10-07 16:39:00 | NPP-375 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 402ebb55-aece-3a48-87bf-04680f364c96 | -4.92302 | -55.87028 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7a29948d-4b7a-3921-960d-cbeceb8944d4 | -2.94152 | -54.14835 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 7a4637e0-d775-3607-b4e5-f6861f389add | 1.7331 | -56.07833 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 0343f833-9341-3764-bf06-0fede13aad0d | -0.77674 | -49.27141 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d65d0c0b-9b06-3501-80c0-b924434de333 | -1.8628 | -44.98144 | 2026-10-07 16:39:00 | NPP-375 | SERRANO DO MARANHÃO | MARANHÃO | Brasil | 2111789 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 85d45e55-f6d8-3748-8ac8-cdf82256eb9b | -3.44608 | -50.63091 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 24945fdb-a79a-3467-879e-1cada230888b | -3.07023 | -54.25338 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9a5aa67b-73fa-3bbd-abd4-e6956aa15376 | -1.53235 | -46.29063 | 2026-10-07 16:39:00 | NPP-375 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 670b78b5-779f-38e1-9216-50c9bf9f28f1 | 3.21315 | -51.2918 | 2026-10-07 16:39:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2d330957-b624-36f7-b71b-6789da7ea8a2 | -4.35345 | -55.13201 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| aad1863a-ba6c-3b26-a372-ca73ef43232c | 1.8155 | -55.53368 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 518ca63f-f67f-3862-9573-e8a78fdacbcb | -3.28058 | -54.04049 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 12ac77dc-1e5c-3579-870c-29b65555a336 | -1.2116 | -49.03835 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a20094b4-7baf-3162-b932-2a6e64cebf71 | -3.173 | -54.60851 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 08597c66-2888-3528-b225-9b7e9137031c | -2.43392 | -56.53609 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7b5d6199-0303-3633-a454-68b353d8a1d4 | -3.29342 | -54.05269 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| c7dedaa5-540c-371e-8710-fcc379ce4e2a | -3.10564 | -54.15165 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a12af2af-acff-3ad5-8a5c-940b09cc7294 | -3.52469 | -54.66687 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dc5555ea-b4e8-3bf3-a6c1-ebb3fdf1dfe8 | -3.53836 | -50.08937 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a97c4af8-e4b0-3c60-aeb9-72b6931da3b2 | -3.3016 | -49.12723 | 2026-10-07 16:39:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 42d596eb-7c34-33d6-a691-e2d69f2ee801 | -2.22118 | -53.70407 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 105d2029-49c5-3459-a643-1aacbbb558d1 | -3.03537 | -53.93512 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 404d1588-6e74-34ef-ab75-4dd14fcc7996 | -2.79888 | -54.09165 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d273afce-7a7e-35ed-aade-e358be9ec225 | -3.52356 | -54.65926 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2ccbdca7-9e42-35d5-a5b3-b0577f0a79b6 | -3.40455 | -58.0226 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c33bd05a-7704-3e1f-9c57-4b4a6bd1eda1 | -4.60176 | -56.07697 | 2026-10-07 16:39:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b06aa5a8-33c5-3704-b73e-3ed69f7d450a | -3.0789 | -54.27362 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3966e865-8ad3-379b-b6cf-14a18c2aa4b5 | -2.79736 | -54.08152 | 2026-10-07 16:39:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8b9ee7dd-5a5c-3ab8-af5d-86117490e782 | 1.72455 | -55.60851 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bdf5845b-f018-3eb3-8392-30852371d057 | -0.80814 | -49.17525 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 68533a91-7f4a-3500-8e94-1e3bd6ccd6c1 | -0.80438 | -49.17582 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ff7ecf49-5846-3657-9ba4-7212f3cbc96a | -1.29446 | -54.5589 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 888cdf84-4ff3-39bb-87fb-a9f3162c972f | -3.04124 | -53.9004 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 032c816a-8fe5-386f-a9b1-a2e12a8349a5 | -3.09524 | -57.64135 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 74e962fb-efae-37e4-99ba-546068a7b507 | -3.39662 | -58.0171 | 2026-10-07 16:39:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f068680c-87ba-3522-a419-4fb52e9cf856 | -3.59267 | -54.56413 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 89465763-3c89-306b-87b2-d10207a2bfea | 2.06622 | -50.87366 | 2026-10-07 16:39:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b1c60ecb-8f01-324f-ae91-f31a85c23719 | -3.63162 | -55.51705 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| ae7bc8ad-62a0-3e9d-9e9a-cfb926327bbb | -2.75226 | -56.60769 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3787237c-fd89-3336-bde5-c1e8ee98c138 | -3.04803 | -53.90954 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| f567b32a-c51a-3709-832b-8f7bd0fc2229 | -3.04607 | -53.93351 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README238.md)
