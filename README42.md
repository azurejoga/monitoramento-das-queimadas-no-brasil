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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 212cf696-b9e1-3cc9-96ec-0a63aa11c50d | -9.5923 | -64.429298 | 2024-10-03 01:51:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1fbd35f2-5535-39d5-b6b5-c502cb8d20f0 | -10.3865 | -67.944901 | 2024-10-03 01:51:00 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 859d2e09-d4d7-3373-8255-43f44619329d | -10.388 | -67.952103 | 2024-10-03 01:51:00 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1172f993-5f27-33d5-96c3-6a2ba6bf6af8 | -10.6975 | -69.375504 | 2024-10-03 01:51:00 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 087e4d81-8e25-3c87-91c5-f32f62391848 | -10.6992 | -69.3834 | 2024-10-03 01:51:00 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7a7eef3a-4d9b-3861-af56-9141fbaa4414 | -10.3314 | -67.741898 | 2024-10-03 01:51:00 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c29bf2e4-d519-3e93-8284-11bd8e482493 | -10.6691 | -69.291 | 2024-10-03 01:51:00 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 58a3d0a8-1455-3a95-b8f3-03e261adad95 | -9.5471 | -64.323601 | 2024-10-03 01:51:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e51caa2d-8956-36d2-8069-9b10664037b1 | -10.3216 | -67.744102 | 2024-10-03 01:51:00 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 30f2383e-a91b-31ea-a534-07cb6c57a52e | -10.7174 | -69.563599 | 2024-10-03 01:51:00 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 31738db5-9b81-39ab-9c25-045dda2c7a18 | -10.3165 | -67.767403 | 2024-10-03 01:51:01 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 28735ab8-f089-305f-8ff4-f494ecd55f06 | -10.4737 | -68.531403 | 2024-10-03 01:51:01 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 439eaabc-5b07-346f-83c4-472fd13f5011 | -10.5011 | -68.657097 | 2024-10-03 01:51:01 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee76423-b23c-32ad-b575-6a44c64492bb | -10.5027 | -68.664497 | 2024-10-03 01:51:01 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 11c4ceb6-be44-350d-891b-9160705b9709 | -10.5043 | -68.671898 | 2024-10-03 01:51:01 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9e3cdd85-cab0-3ce9-b101-528b015294dd | -10.3389 | -67.962997 | 2024-10-03 01:51:01 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 187afd94-4898-3853-9a1b-0853baf1711a | -10.3405 | -67.9701 | 2024-10-03 01:51:01 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 48014125-2298-3922-8680-529e4ee3e5b5 | -10.2793 | -67.738701 | 2024-10-03 01:51:01 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7f36346d-d31a-3856-87be-0a2f8b699e3b | -9.2558 | -63.341801 | 2024-10-03 01:51:01 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 42d88fe8-8f1c-30f4-bd29-a267c70dd719 | -10.3142 | -67.990799 | 2024-10-03 01:51:01 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 137b360e-b73f-3d6b-a78b-20ac60a417b9 | -10.3158 | -67.997902 | 2024-10-03 01:51:01 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 21552e1d-5556-36c6-a273-11f807a61b27 | -10.3174 | -68.005096 | 2024-10-03 01:51:01 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 01fa864c-332f-3ecf-945d-3f2fafb73c34 | -10.3547 | -68.222099 | 2024-10-03 01:51:02 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f1f977ad-afe1-3114-a831-f6500d443d06 | -10.564 | -69.232002 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fe8a4c47-c87e-3a90-98a8-98beaf6da300 | -10.6511 | -69.637199 | 2024-10-03 01:51:02 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e2f5b64f-9128-304d-b0fd-44739bf59e1c | -10.5509 | -69.218597 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3e5f7362-e02f-3cdf-a0df-413574b9374a | -10.0038 | -66.777702 | 2024-10-03 01:51:02 | METOP-B | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 33f75f22-c788-3ebd-8884-8e4d3af5b495 | -9.7845 | -65.851196 | 2024-10-03 01:51:02 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07589931-9355-3f9c-9241-64069afec6d4 | -10.2652 | -68.001701 | 2024-10-03 01:51:02 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c5fb6d3d-45bb-3c34-b833-7d811907d5ad | -10.2668 | -68.008797 | 2024-10-03 01:51:02 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c365872a-eb08-322c-87e9-83f7da7eae3d | -10.5735 | -69.419098 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bf041346-f61e-3995-8767-1d0c2957d26a | -10.5752 | -69.427002 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 70ce39e6-daf8-3477-a144-eab022a83acb | -10.5064 | -69.155296 | 2024-10-03 01:51:02 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d7470b4b-6a15-30bf-9c38-053c7c69884b | -10.5198 | -69.2173 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 8138bdca-fe21-3ea4-9e20-a34e319892d0 | -10.5215 | -69.224998 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ef014844-cbd7-3466-bc22-5b25d786fb59 | -10.5232 | -69.232803 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 668f2565-ff1a-3654-b70d-d6012e1f6b3d | -10.5383 | -69.303101 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1f25390d-67db-3b0f-94fb-e542ff5cd12d | -10.54 | -69.310898 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 91ea5ac8-1ee7-39f5-a5be-233240d84788 | -10.5417 | -69.318703 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7b2c1427-6147-39b7-be48-0e37dc610948 | -10.5434 | -69.326599 | 2024-10-03 01:51:02 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 240a15c3-060c-3c01-92c8-89c3de8298a9 | -10.5116 | -69.227203 | 2024-10-03 01:51:03 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1b957403-9f2a-3f97-97bb-cb92e54df189 | -9.9506 | -66.724403 | 2024-10-03 01:51:03 | METOP-B | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e2b0051e-6cc2-3d62-a947-258720cf66ad | -9.9817 | -66.862801 | 2024-10-03 01:51:03 | METOP-B | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| cf932778-1030-35d2-a3ab-1497957ae35b | -9.9832 | -66.869698 | 2024-10-03 01:51:03 | METOP-B | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 671c270d-4df3-355b-ac5a-1d0fa9355e76 | -9.1866 | -63.442299 | 2024-10-03 01:51:03 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 37981e11-4efb-3c3d-aeb1-283ae78f85ab | -9.4404 | -64.5308 | 2024-10-03 01:51:03 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7e1ce4cd-d944-353e-a3a6-d519c0a08ccd | -9.4422 | -64.538597 | 2024-10-03 01:51:03 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8bfa5150-81cb-3659-9100-f1879148ba88 | -9.4744 | -64.677803 | 2024-10-03 01:51:03 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2b491125-f4fb-3e96-a31d-eed218943b7f | -9.4762 | -64.685501 | 2024-10-03 01:51:03 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4c74705d-6a1e-360c-9301-a6f1656de1ed | -9.4306 | -64.533096 | 2024-10-03 01:51:03 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 371115ab-45e1-3949-86d5-6bdd11fe15b6 | -9.4324 | -64.540802 | 2024-10-03 01:51:03 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9a6383b-8e1c-3a11-ba81-883d3f947841 | -9.4342 | -64.548599 | 2024-10-03 01:51:03 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1f851de1-2a8e-3fcf-b48b-39132c6b1be3 | -8.8908 | -62.323101 | 2024-10-03 01:51:03 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 153740a9-8484-3b26-aa58-1205b3ea9f5f | -10.4475 | -69.168098 | 2024-10-03 01:51:03 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| de7f5043-12b7-3016-8b6a-1d8aa1d6da3c | -10.4492 | -69.175903 | 2024-10-03 01:51:03 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6bc014ed-ec8f-3c6c-8b72-1db98bdd0a7b | -8.8787 | -62.3153 | 2024-10-03 01:51:04 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 800a1717-6704-30c8-a811-382cdba633a0 | -8.8811 | -62.3255 | 2024-10-03 01:51:04 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9905e22-0c2c-36e6-b4a4-1d7cfd2647dc | -8.8835 | -62.3358 | 2024-10-03 01:51:04 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cb8c7846-ed3c-3169-9914-198f08bad613 | -8.8713 | -62.327801 | 2024-10-03 01:51:04 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b390284a-f923-373a-b60f-c4bf3eaf9cf9 | -9.9136 | -66.834602 | 2024-10-03 01:51:04 | METOP-B | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 992e4634-66be-37d5-9bd2-647e573a922a | -10.11 | -67.717499 | 2024-10-03 01:51:04 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f56b6af3-a712-3fa5-96dc-d8d91551c827 | -10.1115 | -67.724503 | 2024-10-03 01:51:04 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb0ac30-38de-36db-96da-cadeb07a0694 | -10.3148 | -68.698097 | 2024-10-03 01:51:04 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0888e885-3ecd-36b1-a063-3829070bcb93 | -10.3164 | -68.705597 | 2024-10-03 01:51:04 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d563df3f-f2e7-3947-88ac-84737486097c | -9.6443 | -65.733803 | 2024-10-03 01:51:04 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 527443ac-f6b8-374c-9f6b-139947db2801 | -10.105 | -67.881302 | 2024-10-03 01:51:04 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 72e253ee-5fd8-33e3-90ef-4074855ec9db | -10.133 | -68.008797 | 2024-10-03 01:51:04 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4bcd3633-c32f-3f19-b997-c9fd6a4d95c6 | -10.1675 | -68.165703 | 2024-10-03 01:51:04 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e089759c-0484-38eb-99c4-f50a20b0ab25 | -10.1691 | -68.172897 | 2024-10-03 01:51:04 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 560b1d2d-a369-3539-bd7e-b4e57a9caaf6 | -9.597 | -65.661903 | 2024-10-03 01:51:05 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 83fd4e85-86ed-3d47-9485-b9395275b910 | -10.1201 | -67.996803 | 2024-10-03 01:51:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 79f2259e-46a7-312c-a531-e313e96c59b2 | -10.1217 | -68.003899 | 2024-10-03 01:51:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 43af1d39-cbdd-3284-b5b7-980428048c62 | -10.0714 | -67.822098 | 2024-10-03 01:51:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f0d524c5-5367-3ad2-bfe7-85ea5c729a1d | -10.2657 | -68.755699 | 2024-10-03 01:51:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c5e28870-2dc9-3724-84a6-ee990d307118 | -10.2673 | -68.7631 | 2024-10-03 01:51:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7c07edfe-8693-34ef-9161-a53583a565d1 | -10.2559 | -68.757797 | 2024-10-03 01:51:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1298a9fc-e783-3ae3-a775-0ffaa787321c | -10.0451 | -67.842796 | 2024-10-03 01:51:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6aa4b2a4-eb2e-3fee-914e-5602518d59b1 | -10.1533 | -68.334801 | 2024-10-03 01:51:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0b57cab9-b0de-37cf-988f-fc0509bcdce8 | -10.1707 | -68.414497 | 2024-10-03 01:51:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 04bec9a8-bea7-3dd4-86f6-9d9ebc86a48d | -10.1723 | -68.421799 | 2024-10-03 01:51:05 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e14bfd46-5bb6-38bb-a29f-6c2689ad53e1 | -10.0644 | -68.024002 | 2024-10-03 01:51:06 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 77d5752a-851b-3059-a431-5d07673898aa | -9.8995 | -67.325203 | 2024-10-03 01:51:06 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0a51dc87-6ffd-3fdf-bd17-2d3d0c6abd77 | -9.9011 | -67.3321 | 2024-10-03 01:51:06 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0b29a9f0-f105-3e79-9263-b2421a1c6558 | -9.8897 | -67.3274 | 2024-10-03 01:51:06 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| dffa4bb5-8c5e-3419-9597-3a3f2ba0de68 | -9.8913 | -67.334297 | 2024-10-03 01:51:06 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 75a21de9-f60c-3e36-841f-051c2109b8af | -9.8799 | -67.329597 | 2024-10-03 01:51:06 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7a5b8e1e-83af-3fad-8978-e2ee2db4e28c | -9.8814 | -67.336502 | 2024-10-03 01:51:06 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c10a356a-eae6-3872-9850-ab6528806f0f | -9.8669 | -67.317902 | 2024-10-03 01:51:06 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b8446211-434b-34ca-981b-f77d4b6e78f7 | -9.7489 | -66.835503 | 2024-10-03 01:51:06 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d3ce2b9-524c-31d4-95e7-e41d34796192 | -10.0736 | -68.2995 | 2024-10-03 01:51:06 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5901e51d-bd53-3e65-9492-c336bd88ad59 | -9.8932 | -67.574997 | 2024-10-03 01:51:07 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b6250ec8-8d1c-373e-a6a9-9103856855e0 | -8.955 | -63.598598 | 2024-10-03 01:51:07 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a06e39bc-dd03-3adb-86d9-0d3d6da9848f | -8.957 | -63.6073 | 2024-10-03 01:51:07 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d67b9212-b9df-3954-b2ae-c76d49384a25 | -9.3746 | -65.4552 | 2024-10-03 01:51:07 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea8471e1-3dd1-3874-a17e-892e8ca04d8a | -9.3762 | -65.462402 | 2024-10-03 01:51:07 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99105a94-0931-3509-808f-5252bfb072ed | -9.3895 | -65.520401 | 2024-10-03 01:51:07 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83fd7433-ba7a-3d2b-96f7-c492ca416638 | -9.3911 | -65.527603 | 2024-10-03 01:51:07 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3feb256-a7ca-393f-9a4f-66d9e7c40c7c | -9.3764 | -65.508202 | 2024-10-03 01:51:08 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aab84bca-67f6-357c-b69e-0e9aaa664b52 | -10.0366 | -68.459396 | 2024-10-03 01:51:08 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 5d8ca57f-6054-30c8-96fe-c0b5bf7a81d6 | -9.3103 | -65.354897 | 2024-10-03 01:51:08 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README43.md)
