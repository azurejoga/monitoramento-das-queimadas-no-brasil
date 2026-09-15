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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f697efab-c04d-351a-994b-f1a23500592b | -2.67675 | -57.59389 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4237c646-48cb-3f2c-83a3-8894b258b68b | -7.56572 | -44.9194 | 2026-09-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 301f671e-573c-3732-8762-f43452d6ea48 | -7.1737 | -43.90206 | 2026-09-15 04:32:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d1cc82c-ccc1-3a73-b338-dea293703e98 | -4.08618 | -54.43219 | 2026-09-15 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90d72259-8836-3442-b028-84dea864f867 | -3.93062 | -52.23439 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cccf77d0-4ee1-3ba2-98b5-3d85953172b2 | -3.247 | -44.63479 | 2026-09-15 04:32:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c4a04e5-4eba-374c-b227-2898ec0d2caf | -2.88876 | -50.41418 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b38ed5b3-ca89-3b1b-b703-0ae30a90c963 | -2.6908 | -57.52155 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f04c45cb-3e4f-3221-ace5-c61c67c040d1 | -2.90125 | -50.43705 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d823f1ad-dda5-3e4d-ba9d-a5e9e5d6f7d6 | -2.88557 | -50.41702 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8affd286-955c-34b6-9327-2e84509efd5d | -2.90938 | -50.4123 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c6b07f3a-9ac1-32f0-a4da-990682b81ad8 | -6.05332 | -52.18871 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7b883332-03ab-34ec-938c-a20e22d58e1e | -2.95301 | -50.39345 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5122938f-d1ee-3c9b-834d-4c49d9275ca2 | -7.76335 | -45.1828 | 2026-09-15 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b355b58-8ccc-3fd5-8da5-f233b8e22e63 | -2.92042 | -50.41929 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6f30cf82-f69f-381b-b1e3-4408a87c701f | -4.55695 | -50.4636 | 2026-09-15 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd8eadd2-cee8-34dc-b42f-feb1c258d2a7 | -7.56349 | -41.84638 | 2026-09-15 04:32:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c066fa5d-f478-3859-95c8-f8afec4cab78 | -3.54434 | -53.99211 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a1983296-c181-32c8-8392-7941601d8162 | -8.09548 | -43.77684 | 2026-09-15 04:32:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 690a7187-012b-3fb4-b8b3-efa7324b793a | -7.17415 | -43.58981 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 154d8096-818d-3ad3-b881-1ba3ee2b952c | -5.80605 | -53.79913 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 661b6477-5fc6-3cf8-9f0f-2738110dc9ce | -2.68468 | -57.59537 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f86e2eac-fd26-3c36-b374-4632d739ac63 | -3.61228 | -45.52633 | 2026-09-15 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ce40d53-ace5-393b-bdfc-ca2e22c9beef | -2.89668 | -50.41545 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb0253cb-c689-360a-85a7-634d7e651b29 | -5.63706 | -40.8555 | 2026-09-15 04:32:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a282dd3c-5217-313e-ba5b-efd46cc19061 | -2.67829 | -57.59425 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef55e106-1396-3f3e-a3d0-499235a02ee3 | -2.90855 | -50.41738 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2323c21-0b8c-3574-8a66-f420cfb44c9d | -2.94825 | -50.39783 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7d1ae31-952d-31c7-b10f-bb40e0123946 | -6.16154 | -52.73661 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6df0bdf3-7330-3620-a718-0aa249d58f54 | -6.51957 | -44.01997 | 2026-09-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4ed3314-55d1-3a05-b18b-804d89ede58e | -2.96486 | -50.39532 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b3823b1-6f1e-3612-b052-33a27d69e767 | -7.1082 | -41.8083 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b3e0545f-8c88-31e5-8db6-4282245ef9c6 | -7.10623 | -47.48379 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 816dbd40-c854-32f8-80e5-680909d50706 | -3.07301 | -51.20248 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae15c16c-1ead-343a-9a99-b791fb2d9264 | -3.39595 | -50.75217 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a43327ea-8a8e-342e-a943-05085224000a | -4.53867 | -54.93674 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 514b95b6-b798-3821-81e8-ec54a07db04b | -2.82617 | -49.22964 | 2026-09-15 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a79a2ae4-645c-3df4-a4ec-236c2ae05385 | -7.46159 | -46.14384 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f79c151-fbe1-3d8f-b694-4ad273480d3e | -2.68314 | -57.59504 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24e110af-0183-3695-9133-0d91a15e1470 | -7.23135 | -46.1609 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb933c95-c3bc-395c-9188-1be43ba04df3 | -7.0808 | -42.12823 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 676f34bc-354d-3bdc-8510-ee680509df3a | -6.05428 | -52.18591 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| aea5de0d-ef08-3598-9493-7601d21bff0a | -6.14797 | -47.73383 | 2026-09-15 04:32:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2efa18de-e907-3f97-aeee-140f6071c5ae | -6.1565 | -52.73977 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ad1c2af-b79a-3040-b601-ab2ed6786375 | -7.56717 | -46.31431 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bda0184-1464-3b1d-b500-5bf66ed421db | -2.9125 | -50.41801 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 34406b4e-7a92-30f9-ab9d-38e19c21e5b5 | -4.29599 | -49.10597 | 2026-09-15 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b6bb008-f146-3bd1-b4ca-5262b76ba254 | -3.16377 | -58.64399 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93adaa09-2c7a-3ab3-863b-69e5df44428b | -2.81759 | -51.33836 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 247136da-a426-3091-a6c3-7a7e5cd0ba86 | -3.07418 | -50.56826 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09b355ea-67eb-37aa-b8ad-0a272391f4e0 | -2.94579 | -50.41302 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3887b2a0-e472-3ad1-aca2-aa0fe5106e79 | -3.38735 | -50.38983 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2c3b5c5-7764-3fa6-8a45-3e73cb06346b | -2.91 | -50.43327 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 54390411-2279-3db4-8e77-9d89009c2bae | -7.9644 | -43.97752 | 2026-09-15 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17af1ec2-2aa7-3afa-aa0a-61b118ba9412 | -7.07981 | -42.10813 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f84ebb4d-be74-37ea-b829-7f653d8919f1 | -6.95226 | -44.53771 | 2026-09-15 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 152e97f2-5b69-3572-980a-01a6ae40697f | -2.78242 | -51.36855 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf9f6549-145f-3509-8f35-fb4d0eccea6e | -6.29831 | -41.6834 | 2026-09-15 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 83f83499-3071-3fa3-b61a-5cb2e945aafa | -7.21475 | -46.13687 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9044b727-cda4-3b22-8021-09d2680825fc | -4.67889 | -42.08183 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 42be6471-8877-3b23-8030-2bf591f80048 | -4.13568 | -54.01614 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b1e0378-585e-3803-8b89-8f107cea7203 | -7.56286 | -44.9152 | 2026-09-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5102a61c-1bd6-3eca-a6db-be0e02830397 | -7.23302 | -46.17186 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 686b76f4-5583-35d7-a3e5-6b6038b4ec6b | -3.53933 | -53.99142 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 9134ebcc-7a3a-3969-92e5-3ac12588edf1 | -7.09397 | -41.82218 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 02298727-bae3-3497-81e1-af7e80a1429b | -3.09235 | -51.3816 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 585cbf2b-beaa-306c-ad4a-36b6d6f9dc2f | -2.69627 | -57.52782 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15017ecc-47fc-321c-b368-370b19120382 | -7.54605 | -44.88624 | 2026-09-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f239a5c1-d7b4-3114-ab20-0b242a98edc0 | -4.54246 | -43.72666 | 2026-09-15 04:32:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8dfc197-35e7-3580-acae-31b3153b4d0d | -3.96788 | -43.11497 | 2026-09-15 04:32:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c79576d-ad67-39ac-8256-3b4ffd95ecb9 | -3.66551 | -40.58804 | 2026-09-15 04:32:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6b9cc44-7b6d-3aae-914f-067b2f229380 | -3.66197 | -40.58383 | 2026-09-15 04:32:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2cfad537-2037-333a-b914-c5bec700e179 | -2.95452 | -50.40921 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 542e89a2-de75-3611-b0a6-f432effd65e6 | -7.29439 | -42.35764 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ed2ae003-d02a-3fce-b5dd-f2dfc94b5864 | -7.02156 | -44.63279 | 2026-09-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3d324d3-a854-3ac5-83c0-91439bab79db | -3.42378 | -58.21895 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 665d788d-3db9-3671-9237-83c0022f78d3 | -7.2518 | -46.16053 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c822a8db-f962-3e41-9408-6145465e2036 | -5.8548 | -52.10655 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eedf234f-66f0-3d7f-b176-ff82cc830d70 | -6.72665 | -48.11857 | 2026-09-15 04:32:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44af885a-7112-3e86-bbe0-724f848acbd5 | -1.22773 | -54.12747 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 233ead2d-9c95-3f51-8295-12ead48b55aa | -6.72549 | -48.12585 | 2026-09-15 04:32:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d742afdc-4178-32fb-abe9-72ffce2c8c56 | -5.35818 | -55.8954 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67fe82bf-cb7a-3fe5-b415-8d8366824b26 | -4.67063 | -42.08527 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 9e14d5ed-55b7-358a-8b76-9b4476387884 | -7.23686 | -46.1475 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd6b2adb-e614-3741-96b3-7cb4ed37bb81 | -7.7401 | -44.7168 | 2026-09-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bd56233-9c85-3994-b10f-701b1eed407d | -7.1649 | -42.10296 | 2026-09-15 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 190d9945-8fb2-3e91-b2ff-6e4eae0157fe | -7.2253 | -46.17778 | 2026-09-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1fe6eae-7307-38cc-bd4d-fbb56dfc3978 | -8.39697 | -42.21635 | 2026-09-15 04:32:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d56dbcdb-5b7f-3fda-bf64-000703dc3350 | -3.07495 | -50.57557 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1747c90-2ddf-3c87-b036-0a1784a0e255 | -6.02337 | -51.78286 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e869d279-a125-3db2-80a0-744a84923e11 | -3.37872 | -50.39336 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c96fbf96-356b-3205-8e83-9dec7f7dd35a | -2.91499 | -50.40281 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b0dfabb-9944-3369-bc41-c3b4d464541f | -8.3965 | -42.22426 | 2026-09-15 04:32:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 325c7ca3-d8e9-3f9d-b9f6-2a2a924ebc22 | -7.22968 | -46.14994 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9422689-8d84-39fe-b885-316f2ad04616 | -4.68198 | -42.08696 | 2026-09-15 04:32:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 62910f31-6217-3c62-904d-5bddd411d0f3 | -3.25232 | -47.08601 | 2026-09-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4d62772e-0309-327d-894d-a37bfda38984 | -7.09957 | -47.48268 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| befa4f7f-17c1-3b1a-8fcd-3844abea8016 | -3.70573 | -52.09527 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c63352da-0334-3899-87c7-75329327b42e | -3.84513 | -51.76039 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c189dcd8-e9c5-3725-97c4-dd6d3614ddb8 | -6.15126 | -55.70566 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README38.md)
