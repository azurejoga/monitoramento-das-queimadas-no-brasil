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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66a9e0ff-18a2-318d-8559-e70f6e9f1267 | -1.2749 | -53.8573 | 2025-11-02 13:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| db50a3ab-3c40-3ce2-9af8-cd43f1af5e67 | -13.9746 | -51.5151 | 2025-11-02 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0489c65d-2bb6-3019-8593-e9e6f6102049 | -8.147 | -44.4863 | 2025-11-02 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 16c7df63-8777-3869-809d-f043546d2db9 | -13.975 | -51.4937 | 2025-11-02 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e550718c-d7a2-3d1f-b0ce-377e215eda66 | -13.9939 | -51.5126 | 2025-11-02 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e9fd5cf0-9a68-326a-b3d9-aeb76f7c3c9e | -1.2566 | -53.8374 | 2025-11-02 14:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 9baff681-cb4c-3104-a503-6ece33e48543 | 1.0028 | -51.2277 | 2025-11-02 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 73.9 |
| c8bd68a7-e38b-3691-9a96-74e4d7fade0e | -8.1658 | -44.4844 | 2025-11-02 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 146.9 |
| edea006c-f9fa-3565-8e1c-110e0851e5ee | -13.975 | -51.4937 | 2025-11-02 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 2bfeaf4b-e5c5-3409-af7c-4a6c89af9b7d | -13.9746 | -51.5151 | 2025-11-02 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9fd16fee-44b3-339a-9c11-863703523ccd | -7.1612 | -41.8154 | 2025-11-02 14:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 3882cce2-705c-385f-95e8-e3d76b4a65e7 | -1.2565 | -53.8575 | 2025-11-02 14:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 7e499c7c-c83f-3e78-be01-337524187de5 | -13.9746 | -51.5151 | 2025-11-02 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 06e97b06-b299-3d70-b7fb-35a029954d22 | -8.147 | -44.4863 | 2025-11-02 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 8785f75f-0c37-34b6-8678-5d5307b5d44d | -13.975 | -51.4937 | 2025-11-02 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d5f1d88d-f280-3dd1-a9c2-5085b2f7e817 | -1.1531 | -49.1483 | 2025-11-02 14:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7f6049b6-a203-3f0c-a733-f257d9672609 | -13.9939 | -51.5126 | 2025-11-02 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 18a07372-4bb1-3529-a8ca-d6ff6e0755c8 | -10.2656 | -44.6067 | 2025-11-02 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 922d38de-995e-3358-8bb5-b95b87f8b720 | -1.2566 | -53.8374 | 2025-11-02 14:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| d2b75e80-1799-3b7d-8f43-dd5c866a7843 | -8.2225 | -44.4784 | 2025-11-02 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| e3970a0b-279f-3f3c-824b-c86e262891a4 | -8.1658 | -44.4844 | 2025-11-02 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f34a04c4-b7a5-3224-940a-a99629ad5bb1 | -0.84 | -48.618 | 2025-11-02 14:10:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6fbfde9f-770c-32e6-85ac-13704e2157c8 | -10.2663 | -44.5603 | 2025-11-02 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 93080096-e3e2-3103-a3d5-5c0ddb54ad83 | -10.285 | -44.581 | 2025-11-02 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 98fbfef5-f1dc-3b19-9c74-cee38b7b755e | -8.1658 | -44.4844 | 2025-11-02 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| d0edb0d1-9d95-30ed-9b7c-9ebbf1aee863 | -10.5289 | -44.8029 | 2025-11-02 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| dd70d92e-d738-3a91-b680-890a3ac85703 | -13.975 | -51.4937 | 2025-11-02 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| bf6a3963-48fd-3c9a-9930-04fe3b5cee38 | -10.5098 | -44.8055 | 2025-11-02 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| dc081db7-3a67-3d85-88c3-4d4c7209c86b | -10.5461 | -44.9159 | 2025-11-02 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d60a3466-0147-34f4-87a6-6d61b54e05d0 | -10.266 | -44.5835 | 2025-11-02 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a19761d2-8f79-3113-a9f3-e8bee1ce8df7 | -1.2565 | -53.8575 | 2025-11-02 14:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 3ebd83b6-1e24-3c33-b4a7-56bd6eea8d5f | -10.2854 | -44.5578 | 2025-11-02 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 76e1d936-f07e-302c-849c-32ea5296d85e | -13.9746 | -51.5151 | 2025-11-02 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 2cbbb84d-6c68-3ae6-8115-278b300e6966 | -10.285 | -44.581 | 2025-11-02 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 691fa97b-9a5a-3097-a96c-b48cdf40625e | -10.7583 | -44.7489 | 2025-11-02 14:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a45cb3df-407c-38c7-a9fa-e81da9b2a380 | -9.8546 | -44.1496 | 2025-11-02 14:20:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 5609f422-da4d-324d-a309-829f45ccd1a2 | -8.147 | -44.4863 | 2025-11-02 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 8a5f6536-6f66-3976-998f-15994b3161c6 | -8.2293 | -43.9459 | 2025-11-02 14:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| b5ab9d08-423b-33e2-a5ad-09d112f884a8 | -8.1658 | -44.4844 | 2025-11-02 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| aa3424b1-eb82-367b-a45c-d4f33024eb3f | -8.147 | -44.4863 | 2025-11-02 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d8367565-12f5-339e-9547-9c5ffa0e063f | -10.266 | -44.5835 | 2025-11-02 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ee36a75d-4ee9-3e83-a94a-88e4c14f033d | -0.84 | -48.618 | 2025-11-02 14:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e9eb24e8-22e3-3561-bfe5-4bfecc0dda7f | -10.5098 | -44.8055 | 2025-11-02 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 24406ae3-e124-3cfa-b060-901fed00d8f2 | -9.8546 | -44.1496 | 2025-11-02 14:30:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 1c85f9f5-5376-3bdb-bcb8-9d85eaecea0d | -13.3177 | -43.4552 | 2025-11-02 14:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 9f037444-6849-3a4e-94fe-bfa1b1874559 | -10.7587 | -44.7258 | 2025-11-02 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 561de408-9ecd-352d-bffe-7cd3cdc545ce | -10.5461 | -44.9159 | 2025-11-02 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 2b9c6cb6-403c-3b32-8dfd-eee66220ff29 | -10.5289 | -44.8029 | 2025-11-02 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e72742c3-c071-3f2d-a04d-02d4d08969cf | -10.7583 | -44.7489 | 2025-11-02 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| cec12de0-074c-3e3c-8c6c-cdff746b0502 | -1.2565 | -53.8575 | 2025-11-02 14:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 69ad747c-cadc-3740-9de3-ae6f16d90254 | -10.5461 | -44.9159 | 2025-11-02 14:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e177eeac-aecc-36a5-bc79-2a20d40f0f13 | -0.84 | -48.618 | 2025-11-02 14:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 432030c8-ad52-3523-a817-21a39460ce8d | -13.975 | -51.4937 | 2025-11-02 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |


