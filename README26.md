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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5dea641b-4aa1-36e2-a848-268328b40f51 | -4.14208 | -47.65677 | 2025-09-28 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d7fcd2c-97a6-313d-bde0-dd413b2c5414 | -5.80399 | -42.8419 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1a7f9e03-8338-32cf-a75e-5bfa0ff6d7c9 | -6.0182 | -46.45451 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c44f107a-b773-30bb-be11-87f72bdf9094 | -6.95404 | -45.39566 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b150db5-c7b1-3349-906b-965542374a6c | -5.41739 | -42.26917 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d71a394c-a641-3959-a49b-f9e6d70046e0 | -5.73016 | -42.8564 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| b56aaf69-4ce7-3f7c-8aba-6449b5e76eb6 | -6.30757 | -45.89328 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 346a43cd-81bc-3a2c-9064-afe249f00569 | -6.24872 | -44.48632 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a8e7f82-1d69-3cea-bf38-e0c68904984b | -6.23146 | -44.65985 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27eac3e8-9d8a-309a-a211-8bd686da94ee | -7.81717 | -45.14349 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90db9f9d-b0b5-3355-abf9-5e0f8b9fef56 | -7.56778 | -42.40835 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c1718229-3d26-3f09-8cfa-99e8d49ce627 | -10.54249 | -43.62897 | 2025-09-28 04:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a106b66e-b6be-3408-84b0-169663288ac5 | -8.26939 | -45.4667 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7111be5-9c8f-31c0-ba2f-485aaf0118c2 | -9.04282 | -46.71543 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b524a5c4-323e-311b-9756-8b67ba8236a0 | -7.75158 | -47.00724 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ce9e1ea-9f7f-35fa-92c8-f5038fbf03c3 | -6.6496 | -43.87571 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87c03232-d1ae-3977-9ebb-a1e5f19c172b | -7.75718 | -45.74952 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95c77813-bf97-31b0-af93-9a502b7e0c46 | -4.95566 | -45.56485 | 2025-09-28 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c0df4f9-7ad9-39ed-9c16-ed623eb685a8 | -6.78082 | -41.75319 | 2025-09-28 04:04:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e9dbc866-8a7b-3719-ba79-d4e61d38ad6d | -5.41387 | -42.26858 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 46c8d591-257d-3deb-b142-e5878f961700 | -7.3717 | -47.03337 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cd029203-0d81-3080-bc31-a450d005184d | -5.80917 | -42.78773 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 679da10f-3db8-3719-97b5-8bd764eeb69d | -7.10475 | -44.23031 | 2025-09-28 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d04d262-7b44-306b-961c-cf77ed7b8e94 | -5.41676 | -42.27309 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 878af106-33fe-345f-a2cb-0e0037c66855 | -5.72778 | -42.66679 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 285c903e-1d4e-34a9-8b18-7deee3d57911 | -6.6067 | -45.09395 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f89d5fb3-a2d9-3751-8597-324192bc4748 | -3.78978 | -48.86641 | 2025-09-28 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b433ff56-5d60-35b2-b0d7-609f1c006ebf | -8.48984 | -44.72092 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c0e9c51-2c35-36f9-811f-710efdc35270 | -7.50541 | -44.3064 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2171f911-ce89-32ac-b22a-bf4717252a92 | -9.06909 | -45.53455 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e07712e-23e7-3be2-9bc5-5be0732ea9b5 | -6.45559 | -42.54103 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3605c22c-3add-3b16-9320-feff676c79d4 | -6.45404 | -44.21762 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e719810e-f861-31fa-be2b-39f7ab9456d1 | -5.71058 | -42.65982 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c555447-9d7c-38ff-81e7-80f22676b455 | -7.03221 | -44.76242 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23db7672-c0fd-37d5-8af7-cb7c37c953b7 | -5.74281 | -43.37704 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 99eee0b8-69f5-302b-bec4-eb6fb62f2e49 | -5.65471 | -43.06799 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 128e5bf9-9900-3ea4-85da-6cd6ff816843 | -5.73712 | -42.83622 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b259e026-0f71-3554-bdb8-c8ad358352ee | -6.99327 | -42.80323 | 2025-09-28 04:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0319aa3c-ca97-30ac-adf6-e1e4af757cf8 | -5.90563 | -43.28809 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9ffde2bf-a7c1-3a6c-a78d-e7a4b8062c7f | -7.30791 | -42.95531 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd6f2d00-2cc3-3153-95ab-6bf6da5a2a5a | -5.74711 | -42.88922 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 324db469-e13b-39ab-ad91-c67d4f072611 | -8.27466 | -45.4603 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35cd84d3-d077-3fec-8544-d4b00e4eea60 | -7.54131 | -46.10337 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc9b51a4-6918-3c77-8a47-cee0babeb19d | -7.38457 | -47.04052 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8bf733d8-a93f-327e-b8a7-b2441f638280 | -7.77719 | -47.02332 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a28cb3c3-2ac2-3fd2-9433-4d92df82a606 | -7.75328 | -46.97004 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd088fcb-d930-3155-911e-c260cd4fdb98 | -5.78015 | -42.82949 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e54ef90e-85e9-3506-bfd9-a8f3da5ef91d | -6.78194 | -44.07755 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 108fac0b-b502-37be-a697-e38bc600925d | -9.38196 | -47.61435 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2244a7ee-5087-32a3-85ed-eaf99de7aa1d | -3.64888 | -48.32579 | 2025-09-28 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7347aae5-a2a0-3bfb-b7f7-275cbf4823a5 | -7.10779 | -44.23566 | 2025-09-28 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 276bec97-2ae3-3612-b884-7a8fc6b15710 | -4.86093 | -45.75846 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c5ab764-de68-3b9c-8948-754bb31bbb8d | -7.18059 | -41.71932 | 2025-09-28 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3dcac882-1102-3217-9876-ade18e4ed549 | -5.61699 | -43.36686 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2e5f791-df29-339f-837f-3e848642bb8d | -5.76599 | -42.79453 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f245d6bc-8a51-3103-8594-0c80098c6bc0 | -5.3649 | -42.28072 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ca00912a-f6ec-3cb1-9c93-b405711192f1 | -5.31659 | -42.76085 | 2025-09-28 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 44c9d864-46d1-350f-a603-7db6a0bfad7f | -6.25095 | -42.46909 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 217471dc-166a-316b-b01b-703fc5480523 | -5.80557 | -42.78719 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4237fb8f-e1ea-3b69-8da7-fd5841c443b7 | -8.47972 | -47.81468 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3406a63-3b7c-3d93-b422-8f79872dcba6 | -7.57125 | -42.40895 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 440ab1b1-4c13-396c-b824-6d582e984e3f | -9.29679 | -43.21652 | 2025-09-28 04:04:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b987922-b8c1-3ce2-9bd8-4b46a7ba08e0 | -5.78753 | -42.85206 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f4cc7240-04ed-3c62-ab54-b108a156973a | -8.49977 | -44.73241 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 75e25f16-fd31-392d-8c33-77565a4cc252 | -7.16793 | -45.50836 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9877d259-8252-3dcd-a5a4-5e92397bd1b5 | -5.76106 | -42.80229 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 55dcefa1-43a5-3c9c-9b5b-a89654e25e72 | -5.82423 | -44.44651 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| efc8fe11-0a6d-37a5-96a0-37e0fc2a9fd1 | -4.19508 | -46.25769 | 2025-09-28 04:04:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8b15b0f-f445-3e61-a921-c9db335e04c2 | -7.20993 | -44.53518 | 2025-09-28 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ed87294-b546-390f-a140-fb39ddc9b04a | -5.82982 | -44.43699 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 408d4e32-7c68-31ca-9934-b6af0227adfb | -6.6073 | -45.09039 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f4693b11-d951-3c23-95cc-2fd91859b7cd | -8.18036 | -41.65168 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 22262168-b2a0-3945-af01-2520aef16290 | -8.10182 | -49.0841 | 2025-09-28 04:04:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30a88923-45c4-3a1a-b025-3edad0b96550 | -5.8211 | -44.44087 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 548ad5b8-1b31-307b-a980-1440181d62eb | -5.95154 | -42.89444 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 19cff949-756c-3d98-a30e-f16fc7c9da81 | -2.58278 | -48.40233 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 21cbd246-a819-3ab6-963c-725128c7e463 | -8.644 | -43.99459 | 2025-09-28 04:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa9bd8b8-0909-3d99-acea-1b71cef6641c | -6.31746 | -43.46052 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa798102-7e99-3e2c-8de8-75c8a0669b22 | -8.2939 | -45.44525 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad52f953-d728-3ea2-aa32-2ca42bf96070 | -5.92716 | -44.61468 | 2025-09-28 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc538720-f05c-32d8-aa48-a92a4200e133 | -6.76418 | -44.58891 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47a62d97-6ccd-348d-914c-8da892c44c4e | -7.15752 | -45.51072 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f297a829-00ff-3e34-b929-00d50f3d7c2c | -6.78279 | -44.04911 | 2025-09-28 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47f38ca2-c57f-33d0-817a-0dba2035b8fd | -4.23161 | -43.71069 | 2025-09-28 04:04:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b0fdb5f-a5af-34f5-b989-f968c49c4ec3 | -4.87033 | -42.9593 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f5f4c840-46e0-305b-85e8-edd2f72307a1 | -3.91803 | -42.18634 | 2025-09-28 04:04:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2275a22b-5598-3a74-b2ce-32abe9131e99 | -5.10475 | -46.07709 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca494b24-4819-33e7-a471-46f79245485f | -7.92752 | -42.67506 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f61c0efc-5bee-354f-9ae5-eb45a6a4ae83 | -10.11698 | -45.66017 | 2025-09-28 04:04:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8652ccbd-7eb7-39da-bb14-2e596c813bfa | -5.89174 | -46.0438 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50eb9edb-0191-3b16-b1d9-89ecae99c0d3 | -6.31522 | -43.45121 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56e01a32-f167-3586-90ce-316dc9d0e854 | -7.23526 | -44.76961 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6da1dd2-10f9-3735-ac7d-88ea6d224993 | -6.69915 | -44.57108 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bde8ec6f-caa6-3a31-8d82-4c3ce77ac752 | -5.93759 | -40.25119 | 2025-09-28 04:04:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6689b42d-c9b6-386b-9cc2-3c2cc73b78ae | -7.75 | -47.01651 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7928284-8f39-3f33-abd5-1d9438984e92 | -8.71921 | -47.98494 | 2025-09-28 04:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 66d12971-a2c0-3492-ab23-a59418576a7b | -9.29826 | -49.10565 | 2025-09-28 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf19a13c-fcc2-3b87-8f2e-3bf7e4e2295d | -5.99739 | -43.92236 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fff1b5f-62c8-3ca1-bbef-d9949042ca1b | -6.0947 | -49.40065 | 2025-09-28 04:04:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ab139f14-6eda-3da0-9de1-53e5e75e2c08 | -10.1249 | -45.33228 | 2025-09-28 04:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README27.md)
