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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88c423bb-5019-321b-ae10-8e2b0a52b53c | -4.90959 | -46.70251 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 236edf30-d854-33c6-b96a-39f232643c88 | -4.90904 | -46.70601 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0980dbfe-cf00-39ea-b9e2-99a10f65fc4d | -4.90849 | -46.70951 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1b04a26-4a24-3c88-a432-3f8f05f77859 | -4.90793 | -46.71301 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57ac6846-6d8b-35f6-9904-87d76bcef171 | -4.90461 | -46.71251 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2089035e-f983-3623-a342-24faec29ce4a | -4.84324 | -46.52105 | 2024-10-11 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 660edcc9-ab93-39aa-9427-1b7a0c51039c | -4.83716 | -46.51653 | 2024-10-11 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec5e3d3d-6bf2-3299-9b33-d8d903dc5584 | -4.80942 | -46.98882 | 2024-10-11 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb87f87c-397e-3109-84a7-b42b608e6964 | -4.67962 | -46.438 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da68c619-f1f1-3dd5-bbfe-19d90928ce71 | -4.67634 | -46.43744 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a418c44-e3a1-3990-a810-061eaef3b6bb | -4.67579 | -46.44091 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6d5d5be-e14d-30ed-97a6-dde3e8330130 | -4.67303 | -46.43692 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eba5cce6-5d12-3096-9dde-dff8f8544603 | -4.67248 | -46.44039 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcda5835-ecab-35eb-bdd0-7c2331e1fe5b | -4.66917 | -46.43987 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ee9626a-38a9-3039-a5dd-3362bbda34c4 | -4.66749 | -46.42897 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8725cf94-89ef-3add-a355-8d0b7dc77463 | -4.66694 | -46.43243 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47ac5556-2bfb-3ed7-87ec-ec3f2703755f | -4.66363 | -46.43192 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88b3358d-3a6b-3700-8f67-86d94c8d907d | -4.66255 | -46.80302 | 2024-10-11 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 619e4c73-a5c8-3f6a-8313-2ca587efeacf | -4.66199 | -46.80653 | 2024-10-11 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45e0e995-3729-3ebb-9eee-b5e6c319af59 | -4.65922 | -46.8025 | 2024-10-11 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e87db848-a45e-30b7-a096-5408e4576b48 | -4.65922 | -46.43832 | 2024-10-11 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 732648c6-c81b-383d-9836-e2f41c0eb04f | -4.65866 | -46.80602 | 2024-10-11 04:23:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44ef528d-18fd-3413-a7ca-1639fc2c6c8b | -4.21362 | -46.89124 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e8028a2-6e3c-3201-b296-91fcb46161ba | -4.21306 | -46.89478 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 782bc9a6-576f-3d7d-bd64-8bc2d01b8d9f | -4.21249 | -46.89833 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0440cc44-ac29-3c35-9973-2123c7584421 | -4.21028 | -46.89071 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98bb1344-881d-32b1-b695-d4cda2fb0ac9 | -4.20972 | -46.89425 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c04591e-0517-3d31-a2eb-67148c266236 | -4.12718 | -46.68677 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4f622a9f-8090-3f86-b88e-191a7c78f818 | -4.1244 | -46.6827 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6bc4cab-cf98-3c5b-be8b-90a7ae6ffa8c | -3.94878 | -46.44021 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f9ae58d-e76f-3ec8-9823-291bddd00f86 | -3.9355 | -46.43812 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7cee2a3a-57ae-317e-b674-07bc5db4def3 | -3.93495 | -46.46307 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c24b6eb3-5d04-3734-829f-b542d625d200 | -3.93218 | -46.4376 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3dc222f5-96c3-38ab-8e69-c6fda028cfdf | -3.92887 | -46.45848 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0d265ba-8ec9-3112-a3cc-13eafbe95e08 | -3.92831 | -46.46198 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d51ab6c9-b817-3048-834c-6a7dc760ab4d | -3.92666 | -46.45098 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe493237-3ab1-3e4a-9077-3c4a468e08e7 | -3.92555 | -46.45795 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87d482c9-fbf3-388a-a7e9-af0f1d6eba28 | -3.92499 | -46.46144 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 07abac71-d5e0-3250-afb2-4fe448604d41 | -3.92444 | -46.46495 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5783ebc5-5152-3096-a445-df7611290945 | -3.92388 | -46.46847 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9d87365-18ff-3c54-b2a2-83c237a034a9 | -3.92332 | -46.47197 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6a278fd-a866-339b-b6e7-371e3e439ea3 | -3.92165 | -46.41817 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60d0f3bb-6579-35f5-9298-96a7b30b7b14 | -3.91177 | -46.45958 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b35bb056-df30-3d81-9b2d-b1ccc1439890 | -3.91123 | -46.46305 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed263fa6-46ba-30a7-ac3d-b6e82d2f8767 | -3.90845 | -46.45906 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c98ae228-5be5-37a2-b47d-2b827a904afe | -3.90673 | -46.42678 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 456f1307-b367-3039-8bc2-7548a12163c7 | -3.90618 | -46.43024 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60a34179-98c3-367f-8e15-1aa8ebb8e13e | -3.90513 | -46.45854 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15c599ca-186b-3302-b85d-ee35f50b58c6 | -3.90126 | -46.46149 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59155c39-24ec-3dcc-8900-490cab3f2fae | -3.89903 | -46.45402 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdd3d469-65ed-3e04-9709-0941163f45f2 | -3.89848 | -46.4575 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ab74b68-b927-34f8-9751-ca69399efbf9 | -3.89571 | -46.45349 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 487b2e29-e3ab-3bc3-9b60-c9bbe229590c | -3.89184 | -46.45644 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21d3da46-82dd-3828-94fe-0cda58e77602 | -3.88852 | -46.45592 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a96b5af5-1f1b-3734-850a-64c508027fa1 | -3.87746 | -46.46132 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d6fe88a-873a-3df0-afe9-2a8e1d739a9d | -3.87691 | -46.46481 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de794904-2e41-3c82-92a0-de52951f115f | -3.87414 | -46.4608 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e532337-706b-3920-b2ea-440045c70956 | -3.85975 | -46.46569 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61864e25-45e0-3658-874b-d0e38ee81536 | -3.85255 | -46.46814 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f2990be-9f3e-3902-9b1f-1f0c23837a26 | -3.84812 | -46.4746 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3323031b-0d02-31b7-afc5-68e6df4cbed0 | -3.84619 | -46.9134 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f41c1022-efe5-3a1b-87c5-e626b7b503c4 | -3.84562 | -46.91696 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a047ed6-a530-3d89-9dc0-02fa8c93c65a | -3.84535 | -46.47057 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5d1787b-ec2b-33ee-8e24-fd34a52c8de8 | -3.84203 | -46.47005 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 974da808-bb57-37e0-826d-50ef7313be67 | -3.89239 | -46.45297 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d37a897e-cb4c-3d3a-8373-50683292a6a0 | -3.87359 | -46.46429 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e0b90f8-c071-34cf-850c-a275a2b54ea9 | -3.85642 | -46.46518 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eed102f-7de0-3f81-9796-1d1ef325b876 | -3.85587 | -46.46867 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e821240b-cea8-3a9a-8393-3fac153f6efd | -3.852 | -46.47163 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40a431f9-1ff9-3724-93a2-54820f714ff2 | -3.8434 | -46.90933 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b96b0f4c-0712-31dc-a98c-d1854132ffbd | -3.84163 | -46.90581 | 2024-10-11 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 081b071f-b57d-36c2-ad84-b982c7f05fb8 | -3.83981 | -46.46254 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e0146b5-0b6f-3269-8523-5f7b808384c3 | -3.83926 | -46.46604 | 2024-10-11 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f13c8cde-741f-39d9-84e0-43ca131ba353 | -3.81269 | -47.49285 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 51d3060d-dac5-3fbc-acda-fa57b500b302 | -3.80929 | -47.4923 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 455d59e8-b04e-3f43-9784-8f2db48101bd | -3.80646 | -47.48808 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb56ec7b-31ee-3edd-960c-c4b4a1848fb8 | -3.80305 | -47.48755 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cf04aa2-387e-344d-8743-930baaee7b8f | -3.70137 | -47.59714 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b9444467-6a82-3e85-86c9-c4446abd8406 | -3.80588 | -47.49174 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2d1aea1-349d-3994-8ddd-40e7f698c1c3 | -3.70078 | -47.60085 | 2024-10-11 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3917d80a-22c9-3a94-a10d-05bb5b005637 | -5.42901 | -47.53939 | 2024-10-11 04:23:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51d73975-591b-323d-9b6e-2941abbc96e9 | -5.39037 | -47.60756 | 2024-10-11 04:23:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1535d1cd-bdac-3f2e-b126-f6fae5c53cea | -5.34004 | -47.79046 | 2024-10-11 04:23:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a58d29b0-11c7-3bf8-96ce-3453d342bb66 | -5.30247 | -47.56462 | 2024-10-11 04:23:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68fa617c-6ae5-370e-af43-6147d9eb85be | -5.26433 | -47.62925 | 2024-10-11 04:23:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c84d028a-4463-3c28-b955-8c7a6c7fe57d | -5.15262 | -47.60388 | 2024-10-11 04:23:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a41449f-3929-3367-a225-701ed9c1d023 | -6.47837 | -46.70835 | 2024-10-11 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a35b5d34-718e-39ca-b09d-979468b5c46c | -5.31724 | -46.57427 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b145a56-25ee-311e-b3c5-29cef8532645 | -5.31393 | -46.57375 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd1ceef3-d08e-3cf7-af37-22f39aab0ca1 | -5.27626 | -46.87492 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90cb3548-1877-36c7-8853-b86b31baf65d | -5.14435 | -46.5717 | 2024-10-11 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6862192b-e648-3596-aba0-a5a4ba1a158b | -6.13013 | -47.2768 | 2024-10-11 04:23:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e069253f-81e5-3617-a136-d20c171a5ca4 | -6.12735 | -47.27273 | 2024-10-11 04:23:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93528fba-dc95-3e01-9999-5358bdc05a0a | -6.12678 | -47.27628 | 2024-10-11 04:23:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 47656202-bfc2-3fe8-9d17-e34e16edcff5 | -6.124 | -47.27221 | 2024-10-11 04:23:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ba6fc9c-3cec-35de-ab4c-eb0c2968a06d | -6.12344 | -47.27574 | 2024-10-11 04:23:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9534287c-ba23-3a65-ba65-69cf47dabf77 | -6.10786 | -47.26603 | 2024-10-11 04:23:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f287fb22-21de-3b60-a751-37126905afb5 | -5.97312 | -47.11131 | 2024-10-11 04:23:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67906f1d-02a3-3e40-b07e-4152c616ff5c | -5.92015 | -47.71687 | 2024-10-11 04:23:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26564fa3-4936-3236-a324-a6af9ab633bc | -5.88561 | -47.82352 | 2024-10-11 04:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README59.md)
