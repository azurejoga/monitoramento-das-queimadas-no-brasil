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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8d16fba-1dbe-3aad-8217-0f4c784e8d8e | -3.688 | -60.59607 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 017dac70-83fd-3701-9bbf-73ccc90eea78 | -3.39287 | -59.58564 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2beaa970-73f2-3622-89d8-c4abaebe0b88 | -3.65732 | -58.57539 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8a1feac-b504-3309-9602-ce781d01ce5d | -4.53287 | -54.97602 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 962039a5-d00b-33e9-9307-de392b9984fe | -3.18254 | -60.65017 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 272080fe-9faf-38a4-9b33-ff6bd1450674 | -3.06862 | -61.2826 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b37913d-764f-39e1-964c-350469a89584 | -3.30832 | -59.45517 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5643c06-7180-359d-8328-171522d9ebb6 | 1.5494 | -55.82413 | 2026-09-21 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fcedcea-60ee-324b-820e-8e887f2cc428 | -3.39508 | -61.29471 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4464a82-0b7b-32de-9338-ce76fc1abc4e | -3.33537 | -59.44025 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50fe6dbf-ed32-3c4d-957c-2ba2eb41e42f | -3.06197 | -61.28156 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21baa421-7eaa-3e1f-bb81-ae6b8506fcf4 | -3.53485 | -58.69447 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1083ecc4-bd7c-3d4a-9672-ebf47cd0fdb0 | 0.26043 | -51.00026 | 2026-09-21 05:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e4c3d4f-19a8-304a-a60d-fdf62f635f4d | -3.53609 | -58.68645 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1797cb5d-c4fc-34f5-b928-08d642a5f24b | -3.19296 | -60.43274 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a43c7caf-5d28-3e9c-a1ab-a85692487f3d | -5.0114 | -56.0947 | 2026-09-21 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 748b24fa-31ae-3fe4-bc35-af8f8ff0f9c7 | -5.01197 | -56.09086 | 2026-09-21 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 339c02a2-fe2f-3c5c-94c1-550b0dd4ff89 | -4.09626 | -52.12057 | 2026-09-21 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 71cc971b-8572-391e-b483-bcca2afc624a | -2.90943 | -54.1453 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bb9cd0c-6eec-347a-b1b5-2b1a96b16771 | -3.64397 | -58.873 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d691db7-46a7-37b2-9c84-33737c65e658 | -3.58824 | -59.06875 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3661bb87-4e32-3e3e-bab3-02de865d9598 | -3.36297 | -61.30383 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48e042c3-303d-30d8-b9e0-bad15aef619d | -2.42328 | -57.13007 | 2026-09-21 05:40:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 246b409b-75ba-3716-9a4b-8a8c2e29615a | -2.79032 | -59.88984 | 2026-09-21 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82c2b78b-4d22-30e6-a81b-be345e965cc6 | -4.34504 | -55.66306 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5d056b4e-b8ae-3151-aa89-d80cdfd73286 | -3.30228 | -57.869 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 252f638e-b3b3-3fc3-8b9d-516703970f60 | -3.34579 | -59.41888 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52a68763-24d1-3f6d-a670-b216b3794eb5 | -3.27242 | -60.88873 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12336584-7db2-35a5-94ba-23c08cfccf6c | -3.49031 | -59.56214 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e22301c-a90e-3231-9c79-3d208fb67b10 | -3.45408 | -58.32376 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5ab987ee-7115-3c18-aeea-4078a64e08f6 | -4.3488 | -55.66751 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 75fb2627-b282-3abd-95c9-565d37c66d00 | -3.07026 | -61.27225 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b7d536f-2a63-32f3-a3b2-d41b49b345e2 | -3.83718 | -56.98495 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8632a9cd-0cb0-3153-a077-1a425fa7a470 | -3.48169 | -59.59497 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c506296-a06b-3ccb-a6a6-ac2be4bb615a | -2.8711 | -57.81453 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cb7ca6a-25c5-3798-b4d7-98aab4a1b3b8 | -2.854 | -57.63217 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3254ce1b-69b2-3ff0-81f1-a55220b7258f | -3.39688 | -59.58246 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29a6540d-eb12-3721-b317-19d1325a4e3e | -3.43859 | -58.23249 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ee90420-1013-37f8-9cc3-ef16d0d3ae0d | -3.33052 | -58.13537 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e9270d1-9b2d-3af7-a35b-231c2e21897a | 0.78808 | -59.2025 | 2026-09-21 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bc49a08-5452-3cd6-93e6-4e087a8276db | 1.5417 | -55.80082 | 2026-09-21 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa9eac65-293f-3c99-88a8-e4e18425542f | -3.98283 | -60.03117 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2062f3b2-65fd-3ac8-8ffd-229956dfd5f6 | -3.45599 | -60.52001 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 945db249-6a3a-37fa-ad09-ab64527a5d6e | -3.10975 | -60.72099 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 145bc4ad-7179-3ae1-bd7b-15a2909d22da | -2.29188 | -57.98683 | 2026-09-21 05:40:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4877e7c8-3494-366c-91a7-d3b2373e1e47 | -3.39409 | -59.53263 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b3dcc66-967d-364d-b7c2-ca29f884ef4b | -2.61571 | -51.73433 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a036058f-9861-36d5-a897-65d8aa513f14 | -4.40812 | -55.24428 | 2026-09-21 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f499942-16f4-32cc-b140-cde2b0e031c4 | -3.90159 | -60.59288 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1eb3f93-ce1f-3852-a524-1509835843d4 | -3.07319 | -61.06022 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b19a6bc-9bed-3e34-97bf-7f32991ef33b | -2.89862 | -54.18365 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcf8cd7a-2143-3e6e-ab47-dc92ca5a3c72 | -3.10883 | -61.41265 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8f78f6e-7378-382d-9739-30ae3e38551c | -3.33536 | -57.88525 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97ecfa24-dff5-3213-89f2-0d90bf7306ba | 1.21343 | -50.97878 | 2026-09-21 05:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4fffb05-2eb8-3728-95b5-978b18d51aea | 1.55242 | -55.82192 | 2026-09-21 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bc3c998-465e-3055-a4b8-91d3092e6d20 | -3.09272 | -61.38534 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8df5330a-1cc8-39bd-bdea-ab8ac87e889e | 1.54561 | -55.80011 | 2026-09-21 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43eb3895-e40c-3e37-8d50-7ff2b55bbf2c | -3.08995 | -61.38137 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 597216ae-05c2-3e4f-b99e-67c2185be647 | -2.64771 | -54.68856 | 2026-09-21 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 704dd934-4367-3ada-9c80-21edbce5841e | -3.42628 | -59.25671 | 2026-09-21 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b62c126-153c-3e61-a1ab-bf88593662d5 | 1.72304 | -56.12809 | 2026-09-21 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cd6e711-44ff-3c66-af30-885bc34b22ed | -3.28813 | -57.86237 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95f6d58d-797c-341e-a148-9e3aee3eb135 | -3.49259 | -59.5701 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65cf8c97-5f19-394c-bf4d-cd65b7da397a | -2.87962 | -57.78466 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85a9961b-8f49-35bf-bd02-b83ae1566c2e | -3.34484 | -59.84857 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f59db05-c9ac-3a0f-98f0-e44f5a6fab6c | -3.30297 | -57.86462 | 2026-09-21 05:40:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d9ce9b9-e465-3bc1-8d5e-27cf3750afcd | 1.54247 | -55.80574 | 2026-09-21 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bc77a13-285a-367e-bda5-0658e62d9f37 | -1.91329 | -58.2602 | 2026-09-21 05:40:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01425771-745c-347a-a590-19af9f89d345 | -2.79314 | -59.89399 | 2026-09-21 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0a97f49-8a4b-3f46-aa68-8b9f3422f4e3 | 2.88529 | -60.0944 | 2026-09-21 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 506ca484-03f4-3ab8-af60-0597256ea207 | -3.39065 | -59.5321 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6227938-9698-38d9-aae8-1168a4dff63f | -3.08227 | -61.17501 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c55e8641-6851-3c12-8a15-7b0627def98c | -3.26963 | -60.88474 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ffab748-3518-3bd1-96ec-33fd955309f3 | -3.14535 | -61.39714 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a958db59-4498-3a46-90ab-6e325b8c6347 | -3.40403 | -61.34568 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a486e53-d40e-3a6c-abba-68ba39ed912d | -3.78788 | -51.92441 | 2026-09-21 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ddc46bd-1104-37d9-bb1e-d1410801598e | -2.45759 | -49.22962 | 2026-09-21 05:40:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2fad940-ea8f-338a-b44a-17a917b79e9b | -3.65831 | -58.85089 | 2026-09-21 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bb8b133-30f9-3fc8-92bd-c36bc29dae6d | -3.06826 | -61.09135 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8e18514-6cf1-3783-8570-9e66fe25530d | -3.01247 | -54.18435 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d54d143a-13a1-3bfb-a979-79ef53434503 | -3.17654 | -58.59436 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5703b47-8545-3c62-bb75-7b50215f68c7 | -3.39841 | -61.29523 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fe85492-ec34-3835-be0f-47fb8b1a18ea | -4.56439 | -55.7524 | 2026-09-21 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bfd84d3c-b5cd-3987-bfcb-b3ed0879a272 | -2.90158 | -59.22161 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f932006-e33c-36d2-a48b-5f3ae75e1ce7 | -3.10273 | -61.15343 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f9310f4-cdb2-3e3d-9880-69da655f1fbb | -3.48683 | -59.60715 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53cfd61b-8af0-3d2c-99c6-810cbfa7cabe | -2.87179 | -57.81018 | 2026-09-21 05:40:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 225942ad-4914-3e76-931c-d6e72252f2d9 | -3.44856 | -50.60401 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 356c0292-3faf-39c2-b07f-b20dc15ef20f | -2.91106 | -54.14725 | 2026-09-21 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d856869-5610-3004-9c79-3c095737b501 | 1.21889 | -50.97787 | 2026-09-21 05:40:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9a90769-4424-3a45-b5c3-f4b930a37f1e | -3.38124 | -61.29608 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a69f171-4788-3f3a-9ef5-b5b093da6d08 | -3.44223 | -58.23305 | 2026-09-21 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab53777b-83c6-3076-b3bb-c27a817c723c | -3.69132 | -60.57497 | 2026-09-21 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29462dc3-024b-3b91-adf8-91a0a6da676d | -3.22506 | -61.04486 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| afc8f718-3f4f-3b2f-bb10-e0ae5204be56 | 0.30423 | -60.4439 | 2026-09-21 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 312cda0e-e4fb-3689-8657-111bce9b45b8 | -3.41742 | -61.29809 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e169af44-69cc-320b-9b3a-01ae7d048211 | -3.44254 | -50.60314 | 2026-09-21 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c19f8d5-69ae-3526-854d-166bfd90171e | -3.47826 | -59.59444 | 2026-09-21 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4063a33-a2cc-382d-a30d-6f655ac30cb0 | -3.33748 | -61.29275 | 2026-09-21 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 296fab88-bce4-32dc-ac6d-f0e56f1764d0 | -3.04586 | -61.25426 | 2026-09-21 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README89.md)
