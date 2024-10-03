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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3aaf36d-93ab-3502-a9a6-08de086bc886 | -12.901 | -62.468201 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| be0b53e4-9b35-33c3-b650-20a7c07e4b9b | -12.9032 | -62.4771 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65ab4dc5-3e60-3752-ad4f-011804200783 | -12.8849 | -62.4436 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bea31c50-a702-3eac-b760-947d144d5b4c | -12.8871 | -62.452599 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1aeba9-5069-3e82-b5ab-9000f64a2c1e | -12.8892 | -62.461601 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 366d7f5a-c58d-3368-9695-7701de537060 | -12.8913 | -62.4706 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4b423b73-0d3a-3d83-805e-6e0aecb36ce3 | -12.8935 | -62.4795 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9d59956c-fec7-391b-93c0-b5fda2eb521f | -12.8956 | -62.488499 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ec0669d3-ce2e-3aa1-9809-c0be4bf18fd2 | -12.8977 | -62.497501 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 995a39c7-0a9c-3ffd-92dd-b6ddddaf1b07 | -12.8751 | -62.445999 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99428236-b084-3718-93a7-da9e872406c9 | -12.8773 | -62.455002 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 67f5bca9-627f-31a1-89ec-c3158d2f3c7b | -12.8794 | -62.464001 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1fe80069-f4b7-317a-a702-f2f415d2a2ac | -12.8858 | -62.490898 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b68621dd-36e3-31f9-a48b-7426965a51d3 | -12.8879 | -62.499901 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 06cc6554-cdaf-3c3a-bb85-9feaf8ceef99 | -12.8653 | -62.448399 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| af9fb703-2d17-396e-b2a4-eb49c48eb906 | -12.8675 | -62.457401 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| feec0fc2-a048-3c13-a895-339fbaabad6c | -12.8696 | -62.4664 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f065abb9-679e-351e-9257-22c9c02d23f9 | -12.8845 | -62.529099 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e1c46fd-d77f-3480-acf7-7dea9905099f | -12.8866 | -62.537998 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 74eb9d89-af0b-3f29-a220-647135575d1f | -12.8556 | -62.450802 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9608bf36-7b53-31e5-a528-a95af6856170 | -12.8578 | -62.459801 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6c49aa49-4e7e-3f25-9db8-17c6ec496496 | -12.8599 | -62.4688 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8bd987b9-c396-35d6-a0da-b9d0518ff8a3 | -12.862 | -62.477798 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e43fe31-147d-3c5a-aec7-a7c15fb90272 | -12.8748 | -62.531502 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b857b179-2ab8-3285-8e50-1f6c0a007890 | -12.8769 | -62.540401 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 32ada357-47d6-3f36-b927-24f5c88aa84d | -12.879 | -62.549301 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a939766c-bbaf-32e4-bd4e-687852d80860 | -12.9125 | -62.690498 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 053ba5c7-c260-3236-8c03-82056c5711cf | -12.9145 | -62.699299 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa59963e-34d3-31ae-8a22-16e2bd2c1f2c | -12.9166 | -62.708 | 2024-10-03 01:50:06 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9c2b5d55-850c-33bf-9b02-8fab1d6841ef | -12.848 | -62.4622 | 2024-10-03 01:50:06 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 14f36b78-40b4-3bf6-89a9-e232181f3d96 | -12.9006 | -62.684101 | 2024-10-03 01:50:06 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3419d78d-2bb9-38e0-943e-0e9789b772db | -12.9027 | -62.692799 | 2024-10-03 01:50:06 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d3d0f681-7ef2-3b24-933b-fc6ac1cb1868 | -12.9047 | -62.701599 | 2024-10-03 01:50:06 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 51fabe07-8416-3540-bffa-752c7a52a92a | -12.8306 | -62.476002 | 2024-10-03 01:50:07 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 352248fc-8d33-3ee5-8731-b6743e93814e | -12.8187 | -62.469398 | 2024-10-03 01:50:07 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4cdda82d-7b1d-304d-ad40-d408bdf39283 | -12.8208 | -62.478401 | 2024-10-03 01:50:07 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7095c580-0e80-3778-a163-e84ffd183a36 | -12.8089 | -62.471802 | 2024-10-03 01:50:07 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54bd8174-946f-3531-aa6e-78a7df16b85e | -12.8111 | -62.480801 | 2024-10-03 01:50:07 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| db7a86d9-b957-3559-826c-18360f930461 | -12.8739 | -62.746101 | 2024-10-03 01:50:07 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c9e46180-40a4-35f4-9187-b9012b1bd669 | -12.8642 | -62.748501 | 2024-10-03 01:50:07 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a96e44b0-bc3d-3f6b-90cc-dcf7831b214d | -12.7937 | -62.494598 | 2024-10-03 01:50:07 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 66c8f4e1-6046-3b8d-bc80-4489da3a6686 | -12.7958 | -62.503601 | 2024-10-03 01:50:07 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d5c12383-fb0f-30f2-863b-a0255e6295e4 | -12.8606 | -62.776901 | 2024-10-03 01:50:07 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 71a28ad2-1b2a-3a61-a25c-c3b132a371f3 | -12.7818 | -62.487999 | 2024-10-03 01:50:08 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9245f7-0011-372b-a578-09a2a00dc041 | -12.7839 | -62.497002 | 2024-10-03 01:50:08 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d41ca85-7497-39c3-b341-6157c61bfb38 | -12.7861 | -62.506001 | 2024-10-03 01:50:08 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f0de2b18-4057-340b-b734-46603ddc3026 | -12.8509 | -62.779301 | 2024-10-03 01:50:08 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07641413-3ace-3e02-8bf1-451da88cac57 | -12.8529 | -62.787998 | 2024-10-03 01:50:08 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2a582477-2082-3291-8e85-5e78ada05714 | -12.7741 | -62.499401 | 2024-10-03 01:50:08 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5fca5164-a9e6-38ba-b7fc-844e91f47786 | -12.7763 | -62.5084 | 2024-10-03 01:50:08 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8d9d43-8cc4-3286-b15b-68c939fb3d13 | -12.8411 | -62.7817 | 2024-10-03 01:50:08 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad0baedf-754d-3ae4-a6a3-809a6b7d2509 | -12.8431 | -62.790401 | 2024-10-03 01:50:08 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c60af39f-1d9b-3ae7-aeef-ee6d2eac68ac | -12.8333 | -62.792801 | 2024-10-03 01:50:08 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3f20e8d-8d28-3331-beac-91ce2221ea4d | -12.8354 | -62.801399 | 2024-10-03 01:50:08 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d39959b-176c-3082-84cd-911a4788c3f2 | -12.7479 | -62.868599 | 2024-10-03 01:50:10 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b3aac0d-f024-361c-bb39-3cf81f5b20df | -12.7381 | -62.870998 | 2024-10-03 01:50:10 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a470eb5a-398e-3490-94f5-3c681fdca99e | -12.7402 | -62.879601 | 2024-10-03 01:50:10 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 14d81ee4-6775-350b-bd4c-2a30174da77b | -12.7422 | -62.888199 | 2024-10-03 01:50:10 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ee425b0f-04a5-3d71-992d-f40a5b8cd95b | -12.7483 | -62.913898 | 2024-10-03 01:50:10 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6381ea-b07b-3974-832b-f12177907cd6 | -12.7503 | -62.922401 | 2024-10-03 01:50:10 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 89ffa98b-a9cc-398f-b84e-ee4c733803d1 | -12.7324 | -62.890499 | 2024-10-03 01:50:10 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5c6513ae-b4a0-358d-ac2a-7e6d6ffa2d31 | -12.7344 | -62.899101 | 2024-10-03 01:50:10 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 129ef318-3989-3929-b194-8d3e18c49f6c | -12.7364 | -62.9076 | 2024-10-03 01:50:10 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a19f810d-e832-3404-900b-dd759f64f0fc | -12.7568 | -63.037701 | 2024-10-03 01:50:10 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a574f51b-505a-3a32-aec2-8d3a719d79c0 | -12.7021 | -63.068901 | 2024-10-03 01:50:11 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 517a006b-658e-36a0-b3dd-0b3df21f339a | -12.6826 | -63.0737 | 2024-10-03 01:50:11 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87571c80-3790-30b9-bb90-36e40c8bee30 | -12.6846 | -63.0821 | 2024-10-03 01:50:11 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b3150dcb-9fa1-38ac-9d37-56ec3b73e5f7 | -12.665 | -63.086899 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 975b73e5-076a-3f9d-9b1d-49616aa0352c | -12.6553 | -63.089199 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d4e6dd2f-45a5-3d52-b57e-1a7d0d2c87cd | -12.6455 | -63.091599 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3595c628-f840-319d-92ab-d769968222b0 | -12.6475 | -63.099998 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e895f2e4-15ea-30de-8aac-5b41e6571ac9 | -12.6495 | -63.108398 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2cdf6ac7-6044-3668-b2c5-dd9cdd68fd0d | -12.6357 | -63.094002 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e4017ae9-376d-39a5-8c1c-a5df5a10b6bf | -12.6377 | -63.102402 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f312b29-e498-3a1f-92a6-bd0646e3890c | -12.6397 | -63.110802 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1d73145a-e1eb-3766-b4fa-8e2a9e62a134 | -12.6416 | -63.119202 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1465b8-919f-3a94-bc1c-3264b707ae80 | -12.6436 | -63.127602 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 88bc7781-bd07-3426-a7b2-fe2678d43ebd | -12.628 | -63.104801 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0911051a-b8dd-30b8-8e8e-63d3d210b790 | -12.63 | -63.113201 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c98afec-1d66-3525-92b2-2e95ad084b4b | -12.6319 | -63.121601 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 671263f2-02e3-3cb9-9d36-edf5296e720e | -12.6339 | -63.130001 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 531714d9-eef3-3c8b-8aa5-01c86325e8b8 | -12.6359 | -63.138401 | 2024-10-03 01:50:12 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2891ea3a-cfe9-36c4-8bfd-012657c4e1e0 | -12.4655 | -62.6791 | 2024-10-03 01:50:13 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 41d944be-627f-300c-83c9-48c5355cfd1d | -12.0474 | -61.025398 | 2024-10-03 01:50:14 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 278512a4-c165-3817-a7d9-86bd153f8548 | -12.3417 | -64.315399 | 2024-10-03 01:50:15 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 66b7bbb5-c057-3de8-9df9-b39e11c901f9 | -12.4024 | -62.980202 | 2024-10-03 01:50:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 003cacdf-4f2c-3987-be08-479ba65a2446 | -12.4044 | -62.9888 | 2024-10-03 01:50:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c700b6e-e63d-300a-8697-3559f42d8455 | -12.3906 | -62.9739 | 2024-10-03 01:50:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 06a561e4-c030-342a-985c-44aa9ada5667 | -12.3926 | -62.982498 | 2024-10-03 01:50:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cba9473b-78e3-34b2-9a29-a22a46183ab9 | -12.3946 | -62.9911 | 2024-10-03 01:50:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b4683ffa-e50d-3f94-818d-4fba22607309 | -12.3966 | -62.999599 | 2024-10-03 01:50:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a75d87e-5fdb-3825-aac0-f39f428b89a0 | -12.3808 | -62.976299 | 2024-10-03 01:50:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 638eafcc-c1c0-3d76-8932-c8ea7a7d5d64 | -12.3829 | -62.984901 | 2024-10-03 01:50:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f49286bf-c3ed-3eb8-b5e8-3b1cfab5cf28 | -12.3849 | -62.9935 | 2024-10-03 01:50:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf7f98d9-50a4-3d72-895e-69953ad843fc | -12.3869 | -63.001999 | 2024-10-03 01:50:16 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 330e9dc8-bbce-34dd-a32d-b8520959c64c | -12.4713 | -64.026497 | 2024-10-03 01:50:18 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c74c9e48-52b3-35fa-9c75-0ea7d8c8bfc6 | -12.0176 | -63.762402 | 2024-10-03 01:50:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7e295e79-8830-318f-a936-ba4e7e359528 | -12.0194 | -63.770401 | 2024-10-03 01:50:18 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 16582462-4078-3c31-b584-6acd416eb7c7 | -11.2471 | -60.5844 | 2024-10-03 01:50:19 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 546d9bb1-9b84-3cfe-b585-04035cec0574 | -11.2345 | -60.5746 | 2024-10-03 01:50:19 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README39.md)
