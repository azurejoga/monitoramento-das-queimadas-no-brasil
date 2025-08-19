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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b96b91d2-b86c-3a60-8e20-3646170b3996 | -14.64668 | -54.89478 | 2025-08-19 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7a24bff-39ed-37e8-982e-98ca2982b584 | -15.03568 | -54.81279 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6b0cf768-b120-38fe-afe3-4950f76efe14 | -15.04177 | -54.81749 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ba13db0-4fd1-3e0f-8c35-2bd9396287d6 | -16.47602 | -45.09695 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30cb22c1-dbb7-3598-a95e-59ece97f1e68 | -19.81706 | -44.32921 | 2025-08-19 04:55:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d78c176b-f4be-391c-b5b4-c3ff8e267ab9 | -16.47684 | -45.09018 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0f6ae6c-d76d-35eb-971f-e56ef619e543 | -17.98656 | -46.35227 | 2025-08-19 04:55:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc1234d2-e7ad-3c8f-9277-8b35a214770d | -19.29432 | -48.43686 | 2025-08-19 04:55:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 503a6d76-0d7b-3e10-89d7-a9e87e780c5a | -13.16334 | -54.94662 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a10c393-bfe0-36a3-b6fc-ad8b81ff6f53 | -16.48822 | -45.08736 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44a62d04-7dc6-3890-9079-68410b8d5c3d | -12.9791 | -56.86161 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b075be5-2ab1-33dc-860f-fbd74570833d | -13.0097 | -56.84535 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27500791-d6bd-3b01-a8db-91bc841a8814 | -12.37486 | -54.16144 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38225365-de07-358a-b27a-0274fdb9f58b | -11.74433 | -58.32961 | 2025-08-19 04:55:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4727264e-d1fd-359c-8cae-5e9587392069 | -15.03279 | -57.19156 | 2025-08-19 04:55:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9dc5f406-398c-3141-bcb7-3c9223e40b24 | -13.25257 | -50.80315 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c99be78-c1d4-3ce3-b14b-7585d21a9038 | -13.15954 | -54.92746 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b68d676-2152-3610-9ca8-e6baee52e16d | -13.58774 | -46.99915 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a805b819-3830-31a6-b983-c63dc9354a34 | -13.17615 | -54.95247 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c664e5c-9011-3f30-9802-609456231a2a | -17.34603 | -47.16518 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e74e10d-e4d0-32d0-9f92-6527a5c86e2a | -14.84856 | -48.05193 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8f3ff3c-a75f-3896-9270-55c38fb1c8f1 | -13.25859 | -50.81279 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7343f675-2163-3e7a-9b56-40e62bd8cd26 | -13.28888 | -50.81104 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1ea1f487-1067-3037-a35f-c948d458017b | -12.98116 | -56.84923 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5a389f6-a0b6-3a12-8228-f06913c181f7 | -15.79796 | -48.22618 | 2025-08-19 04:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 566d9862-0935-358e-9392-d3b3969e868d | -13.30766 | -50.80951 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1abaaf4-1d2a-3041-b9ef-1bc95633c26d | -14.85955 | -48.07083 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 691ed3d6-5bb4-334f-a21b-1ed2727d35d6 | -14.62485 | -54.92422 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96b6a78c-d04b-399f-beda-31da6d26c61d | -14.73846 | -46.30088 | 2025-08-19 04:55:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65ea8685-555b-3daf-807d-16afaa765fc7 | -14.97865 | -54.78489 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6e02c99-df5e-3d17-8bee-67346d6768e3 | -13.01395 | -56.84189 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b1efb44-03ca-3388-96d8-09cbfb3e3967 | -15.79356 | -48.22565 | 2025-08-19 04:55:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49d12834-ed75-3ab5-86e6-222fb4b07ec7 | -15.71356 | -48.63005 | 2025-08-19 04:55:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff18c796-9227-3fbe-bc08-07e127f4be56 | -19.31105 | -46.83996 | 2025-08-19 04:55:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b609407d-178d-3771-b218-2ad4c817dbbe | -14.85347 | -48.04844 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb80e56b-6a93-3fa9-afa8-7290f4555a83 | -14.64611 | -54.89836 | 2025-08-19 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20153aaf-5171-32e7-aa09-4994d7d25f7e | -13.58798 | -47.00617 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80457fa6-5594-3523-8298-f56e5d6f9e54 | -13.18894 | -54.94669 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1a86d16-034e-3b3d-8b2f-017febbd2709 | -13.16784 | -54.93997 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38961210-24aa-319c-ba68-c3cdb8f16be1 | -13.0111 | -56.83715 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e0e8a29-6a32-3eeb-9962-66334615038d | -14.84877 | -48.05411 | 2025-08-19 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef6e0e3d-22c5-343f-bd06-1b61790b70ff | -14.16901 | -45.30935 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6cec525-80c7-3357-8767-fd9b0e69fd7c | -12.98472 | -56.84985 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ebe4930-8ef4-377f-9000-b27f2b35677d | -13.44225 | -56.89553 | 2025-08-19 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4844984-1e6a-34d8-8a8d-77b3754e1f39 | -13.34679 | -54.41177 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 08660eba-1eb0-38f6-9058-db3e8b8a29e4 | -16.62129 | -51.35263 | 2025-08-19 04:55:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4387ebdd-2617-38e1-8e2c-6d228344e09f | -13.16842 | -54.93636 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99c26c7e-3b8d-3d83-9278-eeb855d02966 | -14.17829 | -45.32049 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25a27675-6e15-3691-88b8-a09707336acb | -16.61505 | -51.37015 | 2025-08-19 04:55:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eab00fa1-031a-3af9-8ae7-5e1eacebb437 | -13.31437 | -50.7886 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f9053b4-2166-33d9-ba1d-3d3dc8676d36 | -16.81299 | -49.37098 | 2025-08-19 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7121d316-e123-3931-a497-d878e321bba0 | -16.81638 | -49.36493 | 2025-08-19 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 967a7b2b-e51e-338f-86b0-d322e2efbce4 | -13.47716 | -47.06419 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3cd9813-7b0e-3943-8f35-3e18bb705454 | -12.9848 | -56.84088 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6e923d4-1c38-338f-9f86-522eaa37a52b | -11.74189 | -58.32663 | 2025-08-19 04:55:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 137cb3f2-1983-3a92-9563-b1c05a7b6f9d | -13.74412 | -52.02375 | 2025-08-19 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 458748d3-41c6-3c8b-93fe-34af748a919a | -13.00259 | -56.84406 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 182c7215-61eb-31ba-8294-370a3cd9680f | -16.62429 | -51.35788 | 2025-08-19 04:55:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ba9c47e-2c24-3c5e-a721-1b3a962dc602 | -12.5078 | -57.77977 | 2025-08-19 04:55:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01f17264-d2b0-30cb-910a-1f3c491066b1 | -13.88152 | -54.04473 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff31504f-b96e-3897-8905-e04f1488f754 | -11.94659 | -58.75835 | 2025-08-19 04:55:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44d43a35-b79b-3aab-a80e-f232f43dad21 | -13.59345 | -46.99128 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e088b816-39ec-3ec1-9798-a0da64f06a70 | -13.13447 | -57.16218 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58ac9e72-8d36-3186-a204-81c452301f36 | -13.01465 | -56.8378 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 382f93b7-1afb-3fe8-a83b-d2797f27bcf9 | -17.90649 | -44.4235 | 2025-08-19 04:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ac0be53-69e2-36c7-bef1-f0420f9f690b | -13.30643 | -50.81808 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 852cf15e-d55d-35a7-a008-c98a77c3f742 | -13.43908 | -56.80693 | 2025-08-19 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 703b2bd4-d98d-3a1b-a271-54ecbe612902 | -19.81403 | -44.32734 | 2025-08-19 04:55:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 924cee6d-0a9b-30af-9a39-0c689c113ddf | -13.48077 | -47.08135 | 2025-08-19 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e056676-e30b-3110-814f-beff362466dc | -13.1359 | -57.15366 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97f427a5-11c7-3e74-9bf9-657ec74a7232 | -14.96563 | -50.12187 | 2025-08-19 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82a9aaa3-34ca-32c0-b6f3-d99ed8e7c1d5 | -14.61831 | -54.90102 | 2025-08-19 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5397e4a-9b98-32a4-aba8-baa0a0f5b6f3 | -13.14015 | -57.12832 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c450321e-3ea7-38e4-bc2d-766c8fc21137 | -16.50889 | -45.10153 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5027fddd-b9dd-3254-83f3-3cccae2fe5cb | -12.99973 | -56.83931 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e4f8bee-1d1e-36a0-88d7-ac1f02cb3a6a | -12.98047 | -56.85333 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a36b9d6-98e3-3500-b223-388c5c775c53 | -13.58963 | -46.99374 | 2025-08-19 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afc27a3f-41e8-3edc-8f4d-fcc337ee4b05 | -15.02295 | -54.807 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 782ab144-9a5b-371b-b72d-9a7028a65619 | -13.15401 | -54.91914 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63a68a5d-753f-36b6-98d6-97965de273a5 | -14.98967 | -54.80146 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 295e264f-ff37-3e7b-9c6b-f368daef790c | -13.1424 | -57.15922 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1949cd6f-34a0-3c6a-a9e4-d02834d4c4bd | -13.16405 | -54.92082 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e3f3253-7ac1-3713-aea0-a06ac5038dfb | -14.17308 | -45.31971 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7ba4e91-a602-3edc-953a-05ab60490ab6 | -11.74581 | -58.32732 | 2025-08-19 04:55:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ac38c85-8d26-35d1-ae4b-2be61d3e8205 | -13.13662 | -57.14941 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92fd52bc-e3bf-374e-8c57-4d9f50fdb553 | -16.71093 | -47.62994 | 2025-08-19 04:55:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 533adbe6-d1bf-33de-aaab-fb48438e41f5 | -16.48107 | -45.10122 | 2025-08-19 04:55:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abeb434a-b23d-35eb-b806-b9c5e48c4169 | -13.31376 | -50.7929 | 2025-08-19 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4085748f-cdc1-3592-b9e4-37fb39aa6146 | -16.7115 | -47.62519 | 2025-08-19 04:55:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51671d78-4ba4-31c1-abbb-9b4e0134584c | -11.74765 | -55.84233 | 2025-08-19 04:55:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40288a29-2d15-31db-9b20-68cbb4f426b5 | -12.98483 | -56.86206 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af41011f-e077-382d-b393-133b494389e6 | -13.14424 | -57.15364 | 2025-08-19 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75bc932c-d094-3cca-a618-de182b8563b7 | -13.35068 | -54.40877 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 222faf66-d841-351c-adb9-cc5de3dba94c | -13.86413 | -45.54131 | 2025-08-19 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dda73918-e7f3-3251-9589-6760a54648d0 | -17.82301 | -44.49405 | 2025-08-19 04:55:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e85b5ac1-0bfc-3557-84b8-6efb398cabba | -15.02513 | -54.81474 | 2025-08-19 04:55:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 848da41d-a694-360b-bccd-01a75ff0fa22 | -14.87551 | -48.05073 | 2025-08-19 04:55:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df186b81-ffbe-36cd-ab52-404057532217 | -17.40444 | -46.70696 | 2025-08-19 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 631d55ea-ba94-3779-8f7f-72cb74784de8 | -13.1645 | -54.9394 | 2025-08-19 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28c0c954-f9d0-3bc8-9053-e9874a55882b | -13.34735 | -54.40822 | 2025-08-19 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README42.md)
