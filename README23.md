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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c98e4c3-6934-3822-9ea9-f7c86348ee9b | -6.9593 | -56.37923 | 2025-07-30 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 76558252-07ca-3432-921e-f8bde8a7541d | -5.68155 | -43.67889 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a59eaa0-6560-300a-9034-b83e14081e44 | -6.38672 | -53.32679 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5bae0c9-bd64-370c-b955-5f3ea1b70d3a | -3.50666 | -43.24939 | 2025-07-30 04:27:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 461e06b6-f042-3b6c-87e5-1c1ee897eec1 | -7.94007 | -44.08582 | 2025-07-30 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60a0fa35-124f-3cb6-ab60-9369152f26a0 | -7.21195 | -43.10656 | 2025-07-30 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cc2876e1-1d06-3e52-a355-5dad500e6238 | -8.5181 | -43.30686 | 2025-07-30 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3ca21c7f-3aa7-3ab9-8add-04d3c86f19a2 | -7.60289 | -44.83526 | 2025-07-30 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b5f5448-5470-30c0-9244-e3f6d48d6dbe | -4.29107 | -48.0636 | 2025-07-30 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d1d1c21-dee9-3ca8-b4f0-5c305026f14c | -7.31142 | -44.69029 | 2025-07-30 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b2b34f6-9f26-37ed-a305-54f2805bb45c | -2.9121 | -48.25044 | 2025-07-30 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6f128c79-b62c-3769-96f4-e7a0006c6c81 | -5.76306 | -43.89804 | 2025-07-30 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04eb46b4-301e-3bea-bc19-d33167c471b8 | -9.01902 | -47.97418 | 2025-07-30 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b92a2ad0-11a6-395e-adcd-ea137db6f064 | -6.40726 | -53.37564 | 2025-07-30 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08422e6c-501c-3e3b-84bd-9c4ca0a689d7 | -7.00047 | -42.37608 | 2025-07-30 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7894945-f697-3112-9a56-97899e8c2788 | -8.0152 | -47.6805 | 2025-07-30 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5181e363-ac89-3830-8881-96f13511bf37 | -6.90403 | -44.73003 | 2025-07-30 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64918efa-d0c4-3cf5-894f-508056154f33 | -9.23737 | -50.04137 | 2025-07-30 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fcfc2e7-a237-3286-b45a-4987451b45af | -4.37721 | -48.06934 | 2025-07-30 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34a7065a-55fc-36d8-af78-bab21705615d | -4.86048 | -43.23255 | 2025-07-30 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8388edc3-06f1-35de-a3eb-b4c9bf99c083 | -17.04678 | -43.77647 | 2025-07-30 04:29:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb1e8e20-0780-33f1-b3ad-5c6c33947d8c | -14.23261 | -43.95104 | 2025-07-30 04:29:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06aac286-218e-3fa5-9852-852b1e258885 | -13.07211 | -47.38008 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55ec7ea8-ef65-368d-a24e-8a41e5a556b4 | -14.46029 | -47.87182 | 2025-07-30 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b22f497-7d60-3437-8d8b-5809d0bbef65 | -14.41486 | -59.33858 | 2025-07-30 04:29:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0442921c-bcda-3c62-921f-8d61c5d8abdf | -13.06769 | -47.38659 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e4ca66f-7b97-3f1e-8b4d-7a585cebce22 | -14.76443 | -47.54405 | 2025-07-30 04:29:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b660d315-8773-3a29-8bb9-d808d2ce11fb | -13.53125 | -45.64769 | 2025-07-30 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48629a30-9376-35e5-81d9-5aea82c5afda | -13.41778 | -47.29014 | 2025-07-30 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a730ae2-52f6-3892-823e-af5fc41fbf2f | -14.09899 | -53.97876 | 2025-07-30 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 085ae1f9-df91-3498-9709-8e9b60b261b4 | -15.49742 | -45.92487 | 2025-07-30 04:29:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ed522a2-f9e9-3b46-a648-816b07adbb24 | -13.41723 | -47.2937 | 2025-07-30 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3dc438f-88a7-3785-8c34-64ea6b396fb3 | -14.21875 | -43.93933 | 2025-07-30 04:29:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a203fff8-3f41-30b3-bc47-30498313800b | -14.4139 | -59.3431 | 2025-07-30 04:29:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77cd524b-6dd8-3fe9-9a52-5ad0fa19feaa | -13.14567 | -47.3414 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 120ba98f-d916-3a36-aed0-44f0f5fcd5e5 | -14.22948 | -43.94575 | 2025-07-30 04:29:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f47c1a56-d564-3579-8f28-db88f591a0fe | -14.41145 | -59.34451 | 2025-07-30 04:29:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95c2808b-5217-3bfe-a117-ea9d1655fd85 | -13.66837 | -48.77671 | 2025-07-30 04:29:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdf55f26-821b-3948-b0ab-45b93c6ffe6f | -13.07934 | -47.31202 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33e68967-f8bf-37b9-94aa-f3aef2363e16 | -13.14457 | -47.34853 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c55d1cb-0948-3ad0-9aa0-5fb95f95ba55 | -12.95042 | -48.25739 | 2025-07-30 04:29:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9347b521-a33d-3620-aa1b-b7aea8452676 | -13.66667 | -48.77684 | 2025-07-30 04:29:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bd24edf-8b4c-3cd1-b543-e8c24eb4ecfb | -14.46085 | -47.86827 | 2025-07-30 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8934d463-e4f7-3d63-9cfc-77f8fb826357 | -14.7611 | -47.54351 | 2025-07-30 04:29:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c4f09ca-d37d-3cb4-ad34-86c1fbdc23e7 | -13.08432 | -47.32382 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42adcf09-abdd-3068-941a-0fbe20cbd303 | -13.24833 | -50.13097 | 2025-07-30 04:29:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| beb115b4-3427-3d72-b317-a6bdef460ebd | -13.54451 | -44.14206 | 2025-07-30 04:29:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d45b84a-e5fb-3ff9-a223-d4a7dfaa0c64 | -14.4787 | -47.87869 | 2025-07-30 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac258e26-3e55-39a6-908b-b8db762923f2 | -13.08377 | -47.30549 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6633aee3-6b64-384d-9f34-fe56016b4835 | -14.23128 | -43.96047 | 2025-07-30 04:29:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d909faa4-18c8-309b-9984-b6bfc6804d84 | -14.917 | -45.14666 | 2025-07-30 04:29:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7453cec-3541-3f67-b983-fcc7308b393d | -15.76833 | -49.95754 | 2025-07-30 04:29:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 12c901bd-83be-38f6-bb08-56f5b97e3fcf | -13.14512 | -47.34497 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7cc6529-f281-370a-a6c6-c614daa5f833 | -14.41239 | -59.33994 | 2025-07-30 04:29:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64cdabe6-cf8f-353c-9f04-30ea156b691e | -13.08321 | -47.30906 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c969112d-9a0e-3794-ba18-3d9031c19fc5 | -14.4621 | -47.87594 | 2025-07-30 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e36b7928-d8d3-3342-acd7-f69f8f7fccdf | -13.0821 | -47.31615 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8707bc8f-2f49-3916-97f0-21364897a884 | -14.73975 | -46.30723 | 2025-07-30 04:29:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18910770-e986-302c-9ded-d6ebedc64a56 | -14.74089 | -46.29963 | 2025-07-30 04:29:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70967fc3-b084-3914-b1f5-004f74c4a83f | -12.57713 | -49.79992 | 2025-07-30 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 085cd049-e17a-3f05-8bd2-678f603562a9 | -14.22634 | -43.94046 | 2025-07-30 04:29:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fc40e4c-3d16-39c3-8ca1-a02c8006e674 | -14.21496 | -43.93876 | 2025-07-30 04:29:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ff59007-2c91-3ca3-bf31-ad757ab49d99 | -13.08266 | -47.31261 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7671c300-e8a2-3fc2-a32b-0db23bdf65aa | -13.22658 | -47.21624 | 2025-07-30 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 043ed9e3-0df7-3220-93cb-b1e8043b4979 | -14.23194 | -43.95576 | 2025-07-30 04:29:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86a4dae1-1c49-34a6-9462-68cc162ecdc0 | -13.09153 | -47.29949 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b177c61-1eee-31f3-87ae-9040dda7e3bf | -14.74032 | -46.30343 | 2025-07-30 04:29:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94e8bbdc-22d1-35f9-9eac-6a927409a4dd | -13.06437 | -47.386 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9be55dba-b659-3dd5-90ec-016a7cb25f6d | -14.46266 | -47.87239 | 2025-07-30 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7859de49-5388-3ce3-b792-0d18389e99c2 | -15.76493 | -49.95695 | 2025-07-30 04:29:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 44009c92-d70b-38bb-b66e-c40bce09007a | -13.06161 | -47.38188 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b199788e-0ae9-3e56-b701-e6ad9b259d18 | -16.1096 | -47.91778 | 2025-07-30 04:29:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2b8f65c-6d8b-3460-beec-c5f5732ff3d8 | -13.08764 | -47.3025 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de780b46-ea26-38b5-ab6e-b852d2d9e7c2 | -12.57778 | -49.79601 | 2025-07-30 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bced6dd6-da63-38ff-8955-3dc403778176 | -16.20433 | -48.73661 | 2025-07-30 04:29:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| faa3fbc5-85a8-36b0-80c8-20ea81cc0a63 | -13.08763 | -47.3244 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2506dd63-0170-3889-8332-4b1283b1ae45 | -13.08155 | -47.31969 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af2b0fda-63d9-348c-8d61-5a0ea63bf011 | -14.84426 | -49.28002 | 2025-07-30 04:29:00 | NPP-375D | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e27fd986-1f91-3b8d-9645-42d61b065a12 | -14.09824 | -53.98278 | 2025-07-30 04:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f23c9020-0bb6-3f0b-98f6-4f5e3e58c699 | -16.49268 | -48.64917 | 2025-07-30 04:29:00 | NPP-375D | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b24e346-a1f4-32bf-9825-cf27812dfe09 | -13.53356 | -45.65599 | 2025-07-30 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89332a96-8f09-3130-9130-62d6000b2db5 | -14.50383 | -46.53176 | 2025-07-30 04:29:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89455c05-d32f-3da4-af2b-12232f722ceb | -14.47538 | -47.87815 | 2025-07-30 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6d030ae-75eb-3bbb-869e-2eb147618d4d | -13.09485 | -47.30005 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c389fce9-be17-3ee9-8f0b-97f73a0fb135 | -13.53471 | -45.64822 | 2025-07-30 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fab2506f-fe11-3fa6-9ca8-965ae759cad4 | -13.07156 | -47.38363 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0724a9e7-a44c-3bfa-bc7d-ad800bc2e1fb | -11.34826 | -51.25434 | 2025-07-30 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc89203b-887d-307d-83a4-b437418db688 | -11.46463 | -45.11848 | 2025-07-30 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 29ba6bb1-c6ff-3723-99ce-a863857be019 | -10.93531 | -45.78455 | 2025-07-30 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e472498c-2786-3983-94c1-eb0e2be6978a | -12.46317 | -44.09259 | 2025-07-30 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 957f9d04-1579-3c1f-8f6f-5aba00ab5175 | -10.93586 | -45.78089 | 2025-07-30 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dfa2872-9d6b-340f-8d10-5b3a85fd2430 | -11.98106 | -46.69962 | 2025-07-30 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bf96fdc-f5b0-316e-98f9-0153a8708ff8 | -11.97962 | -46.95061 | 2025-07-30 04:29:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0da9a619-18a2-3499-84e6-4de060ce04e3 | -11.46578 | -45.11077 | 2025-07-30 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f58410f-9d9f-390a-ac76-3e3d2cea3195 | -11.54021 | -44.25325 | 2025-07-30 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4d31077-98de-3c4a-b4db-5a1a389e1da2 | -11.46868 | -45.11515 | 2025-07-30 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b3cbc85a-0981-3b4b-b5ec-a30d60446ff4 | -11.81465 | -44.25977 | 2025-07-30 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec52cab0-1d0a-33fb-8158-b3799ca5933c | -12.46075 | -44.08324 | 2025-07-30 04:29:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d4b7bf3-04a4-3af5-9b39-4b87443c666f | -12.73243 | -47.00198 | 2025-07-30 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 855c4ea6-cbaf-3412-87dc-0fdc3a8a5c9f | -12.81046 | -45.43846 | 2025-07-30 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README24.md)
