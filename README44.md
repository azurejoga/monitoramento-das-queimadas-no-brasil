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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13182cd6-6125-36c9-8713-b7223b245166 | -12.09994 | -50.25816 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1625eb5f-231c-3f93-96f5-79196d73c943 | -12.09639 | -50.25755 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a1bcc1c-2803-3ea8-91b4-5c078d10aea1 | -12.09571 | -50.26163 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b11fff0-b11e-3fba-9872-c487949ebc66 | -12.09328 | -50.32021 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbd00aa0-5db8-3ef9-9769-95c04965b856 | -12.08971 | -50.31959 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34cacc29-dea5-3689-99ed-b78b63b36156 | -12.08903 | -50.3237 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ffa8115-6130-3b14-babc-cf3c9a9e06d8 | -12.08546 | -50.32308 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8053a0b-d06d-3fbf-9d0f-b85785caa735 | -12.07833 | -50.32183 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e2ce10a-ee1d-3770-8647-f022ed1d896f | -12.07656 | -50.26671 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 98ac45b7-2329-35a0-9066-6e5c2f464ad5 | -12.07588 | -50.27079 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7a1d809d-056b-3e63-8312-7490231e66f5 | -12.07545 | -50.31711 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 833ae831-9a20-3f83-a1db-2eafa8be0811 | -12.07519 | -50.27488 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 155171af-cd6b-38ef-9da4-bee15fb5b561 | -12.07477 | -50.32122 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88661804-b320-3950-b14d-5348df82169c | -12.0745 | -50.27898 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81bb9241-344a-3588-a222-34d0de6eab64 | -12.07382 | -50.28307 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a088d57-b6e9-3227-86e7-890289f72104 | -12.07258 | -50.31239 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5db103c-bdce-32d4-9ebc-5f07fd87d8c6 | -12.07245 | -50.29126 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efee038f-a927-3429-a308-bd10ac604c06 | -12.07189 | -50.31649 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c8e3a87-0469-3d74-a493-43e3184673a2 | -12.07163 | -50.27427 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eef9f783-0c79-3a76-bead-c91e6d9564ba | -12.0697 | -50.30766 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13129814-db88-3818-9044-3d0fda086997 | -12.06901 | -50.31176 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 698eeeb7-eaf3-3366-a2a8-9aec8af58ab4 | -12.06378 | -49.47869 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f5390ea-f75f-32f2-8496-04f78a6d71d9 | -12.0597 | -49.48194 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d304ad08-a8b7-3990-9de7-2829f7f767cc | -11.60525 | -49.86786 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3756fe89-e829-38e8-9489-2ba9d5dd12e7 | -11.60173 | -49.86726 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bef5c16-0bd6-3fa4-97dc-caf9a234c6e5 | -11.58595 | -49.83192 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5d5ec68-5592-3d73-a3ea-9a7a705ec466 | -11.58529 | -49.83589 | 2024-10-15 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bd5e9df-2496-3d01-881a-2cec5b172cb6 | -11.18612 | -49.95658 | 2024-10-15 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95b29822-57cd-39b1-aa96-91cec88a7e67 | -5.64567 | -50.33535 | 2024-10-15 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e2792f7-1db1-32dc-8141-6a09b7d4b4e5 | -5.6391 | -50.15032 | 2024-10-15 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e27735a5-9ca2-3bb1-8de2-eeae10315452 | -5.63527 | -50.14966 | 2024-10-15 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7226193-b450-33bf-a6a8-dc7619a80d89 | -5.34205 | -50.95802 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aee7ae15-4472-31db-b714-1a4edfafb80b | -5.26654 | -50.4682 | 2024-10-15 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41f1764f-4256-3b8c-bb10-35e2d3780910 | -5.26315 | -50.47108 | 2024-10-15 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 777fe39f-03a9-3300-90b9-b15fd291fbfe | -6.40919 | -50.78092 | 2024-10-15 04:25:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 852144c7-7706-3676-97a6-8f873bac9ac1 | -6.21263 | -50.89828 | 2024-10-15 04:25:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8109e4a-2861-3586-81eb-256c712c844c | -6.19843 | -50.88538 | 2024-10-15 04:25:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 801269f2-0883-32fd-b65f-8211ae571451 | -6.19445 | -50.88471 | 2024-10-15 04:25:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 610042af-90ec-307c-b102-9f8564d2cba0 | -6.18959 | -50.88928 | 2024-10-15 04:25:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e495c47d-b49b-3955-992f-1c36a440fdd8 | -6.18793 | -50.88717 | 2024-10-15 04:25:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b598f3e4-4de8-3b92-afa5-01d2ebbc4aa4 | -7.72533 | -50.10496 | 2024-10-15 04:25:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89773add-6cf5-34e2-aec2-8a33ad5079ad | -7.09887 | -49.89772 | 2024-10-15 04:25:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17f131c0-d2b0-3110-a13e-7e6116a450dd | -6.85128 | -50.36003 | 2024-10-15 04:25:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79a20f78-554f-342d-95b5-b18bb09337fa | -8.4207 | -50.24247 | 2024-10-15 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f6830bb-08b2-3d4c-a66f-e3accf40507c | -10.66859 | -51.82758 | 2024-10-15 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae4e73da-8a28-300a-be5e-dc14c0427890 | -10.66746 | -51.82455 | 2024-10-15 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d126bdc4-e021-34ca-902c-6e1d870e012c | -10.66656 | -51.82966 | 2024-10-15 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10b7f28b-6b2d-33b7-b966-b843aee3eaa4 | -10.66551 | -51.82175 | 2024-10-15 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee92f23d-fa5a-3a8c-b59d-0c6222a62b93 | -10.66464 | -51.82687 | 2024-10-15 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 319bd17e-1701-3fca-9eca-259dbe9246a9 | -10.42638 | -50.83141 | 2024-10-15 04:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4379761-54f6-3850-8798-bc06534c6eaa | -12.0818 | -51.05924 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f21fb557-ccb5-3490-86ae-044307dc9862 | -12.08105 | -51.0637 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d3df630-4cd8-3207-b349-1b7560342a88 | -12.0766 | -51.06749 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3d351c2-6535-3ce4-a5a4-8b83f75bbfa0 | -12.07585 | -51.07194 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2ef0af7-f599-35be-8aad-9f241a0e996e | -12.0751 | -51.0764 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95dba28f-3c60-3d7a-95b7-3fd1f39364f1 | -12.05051 | -51.10884 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 424c2d25-cfc8-390d-a8cc-8cb85a9418cc | -12.04757 | -51.10371 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 926d4f86-0b5f-3e2d-877c-dfaa00a2ecef | -12.04681 | -51.10819 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3581ce2-d4c2-3252-988f-579a0dd27bd2 | -12.04386 | -51.10305 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdc478c0-a830-3c83-a752-15048fab5f2c | -11.32611 | -51.43103 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f228b55-cba5-3e42-83e7-d6ab00dbbb3e | -11.2868 | -51.45351 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc2b25a9-88dc-367b-8faa-29fbb8d545fc | -11.28591 | -51.44544 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa03a027-7c3f-3d41-8e4c-eba6f6ed22b7 | -11.28511 | -51.4502 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24d61925-41f2-3a8b-9d41-8cd3ff75cc62 | -11.28464 | -51.44333 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38d8bd1f-e3f5-3933-9f71-e89df79616d0 | -11.28432 | -51.45496 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71f0247a-b2d3-3490-a997-a29d83da79f4 | -11.28381 | -51.44808 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 470ba60c-7a73-3544-894a-1fba0831c212 | -11.28209 | -51.44475 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e9b75e5-e951-312a-875e-84fa9e317df2 | -11.28082 | -51.44265 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9f0c7d5-8168-3abc-8f50-a8b1daaa0e90 | -11.27827 | -51.44407 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1f04152-556a-36e2-b8bb-83a2dbafdfae | -11.27445 | -51.44338 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4e73143-f088-3c5b-830c-27a11e49b78f | -11.26219 | -51.44611 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed4ca20b-63b2-3090-a27d-c3477b031ce6 | -11.25837 | -51.44541 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1066eeac-3274-3999-8aa7-60dd64c61418 | -11.2377 | -51.52064 | 2024-10-15 04:25:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6817c2d8-19d5-3e45-9383-021b8239dbb1 | -11.23689 | -51.52545 | 2024-10-15 04:25:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4d56848-ddb9-3016-a1be-15f5d98848e5 | -11.23525 | -51.53507 | 2024-10-15 04:25:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| becf6a41-dc7c-357c-91c7-3f28f6ecbfb3 | -4.66002 | -50.93785 | 2024-10-15 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d319a34e-223f-39bb-a7bf-7d4198761674 | -4.65903 | -50.93821 | 2024-10-15 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b26a6622-f5ac-3df4-bcae-34739f11dfbe | -4.65244 | -50.93273 | 2024-10-15 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 405d8379-f9cf-31f3-bb9c-963a43ee029b | -5.51512 | -51.11528 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52dc16be-0359-3568-81dd-362cb0736475 | -6.51307 | -51.44097 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3a2f76d-a822-395e-ada6-305e6d4d51dd | -6.51246 | -51.44468 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dabfd6a5-000d-3c3d-b8bd-2d18625598dc | -6.50897 | -51.44025 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9676f608-c9ac-3423-8a85-41f0b7295778 | -6.34468 | -51.75766 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36eb655a-86af-371d-8ca4-677e229e1ab0 | -5.94459 | -51.6927 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab997aca-ccf6-3691-abe7-a6f4f916cd75 | -9.3396 | -52.84307 | 2024-10-15 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd96c0a6-5552-3806-8f09-df263d7ccf37 | -10.86282 | -52.3717 | 2024-10-15 04:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eb73dad-f01e-3301-a49c-817c0923d4e4 | -10.86219 | -52.37534 | 2024-10-15 04:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dc24531-eff3-3185-9695-7bd80c7fa643 | -10.20545 | -52.32078 | 2024-10-15 04:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 059cc12b-e45e-323c-9ace-98f4c40920ea | -10.20135 | -52.32004 | 2024-10-15 04:25:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f75ab51b-cd60-3407-b8e3-8749b131c359 | -11.56622 | -53.85479 | 2024-10-15 04:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bdf99d53-9844-3a3f-8b69-57f6afd7723d | -11.56542 | -53.85924 | 2024-10-15 04:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b9616e3-b1ee-33b8-b8c3-f1eeee39f1f7 | -11.56178 | -53.854 | 2024-10-15 04:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f2946e24-7c48-3635-ae17-0a15c4ef6646 | -11.55813 | -53.84883 | 2024-10-15 04:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca59d666-44dd-3b16-956a-645658afda12 | -11.5537 | -53.84802 | 2024-10-15 04:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f553ea8-644d-3efb-b262-c64789a52536 | -11.55006 | -53.84285 | 2024-10-15 04:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bcdb881-1a6d-30b8-b295-6612d5eb0ba0 | -9.00905 | -54.50124 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f9b0891-bed6-3200-b518-03a678a6123d | -9.00808 | -54.50656 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 838d5050-23e5-32c3-8eeb-9df57a47df4e | -9.00531 | -54.50447 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 4c51d60c-967b-385c-926a-5aafe94f9565 | -9.00422 | -54.50036 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8d77f315-f705-3f0e-932c-84f83e1c4e03 | -9.00323 | -54.50573 | 2024-10-15 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |


[Clique aqui para ver as próximas entradas](README45.md)
