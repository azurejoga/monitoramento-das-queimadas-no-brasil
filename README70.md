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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba8a3831-6355-33ef-8c0c-bdccb3e98e6e | -3.1569 | -51.12146 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7578319f-aef3-33e7-8358-d5b666468fb5 | -3.15553 | -51.13056 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72caf81d-b261-38c3-b6c2-a62a1d0e5b46 | -3.15278 | -51.14873 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17f91f8a-1941-33b2-9732-b9c06267c036 | -3.15109 | -51.13449 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89474f69-3be6-358c-8272-7d1618383d38 | -3.14902 | -51.14816 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d08ced1a-16aa-3c91-a421-a6906f557678 | -3.13981 | -51.0299 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 894e72fe-e479-3d60-9d65-9f38d9cb8d59 | -3.13603 | -51.02935 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 74476db3-0ded-35b4-8655-727157b18654 | -3.11351 | -51.12882 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2f88f290-df28-36aa-9cc6-b0ece8b65c77 | -3.11284 | -51.13334 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c11429f3-c971-377c-8452-56546a9d0a57 | -3.11278 | -51.12686 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0e479804-c5e1-3fad-9d6a-170e5bf1d513 | -3.11216 | -51.13787 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de165801-bc67-36aa-ba2d-3f3ef63ef8c1 | -3.11208 | -51.13136 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2ec0d77a-460b-39a4-b3e7-db1abdfd27f2 | -3.11138 | -51.13588 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4778222c-1fe1-304e-8f13-45951b0fc42f | -3.11042 | -51.12375 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cac4284f-4af4-3a99-aac9-431e85860174 | -3.10975 | -51.12823 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 328bec18-7c43-3efa-9571-c5ebc4b81e40 | -3.10972 | -51.12181 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 05c0d769-76bc-39f4-86fe-6510940194ea | -3.10908 | -51.13275 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e4c73f00-8091-3df8-89b9-4fbf60fef11c | -3.10902 | -51.12627 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 62d62e0e-7d0f-3956-953d-33178e4b8e6e | -3.10841 | -51.13726 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9735cbdc-6e58-3a76-8c70-373642a89306 | -3.10833 | -51.13076 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 00ba6356-c117-3950-bdfd-4c50b0bd6c77 | -3.10763 | -51.13527 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 352f9434-d146-325d-99db-c2367f8ce6d9 | -3.10734 | -51.11864 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5557c870-6832-3858-908a-f5db8bc84510 | -3.10667 | -51.12317 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0efd2050-e9b6-38f2-a114-78890c33e1b3 | -3.10596 | -51.12122 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2f58352-d42b-3bc9-b929-728c18e9f079 | -3.07281 | -50.985 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8661519-541f-3445-9a28-36006e804d38 | -3.07211 | -50.98963 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1577001e-379f-3d85-b2c9-e95280b6bd23 | -3.06832 | -50.98905 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c1f2771-4145-328c-93b1-821dca13b21e | -2.9811 | -51.05251 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2bfe43b-0706-3dcc-b489-47dfae5ee672 | -2.95712 | -51.05816 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| de58afc1-89ca-3a80-b5a0-f455484f38c9 | -2.95642 | -51.06274 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9030e836-38a1-3700-a455-168bd7f269c8 | -2.95405 | -51.05299 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20b0769a-0292-3c87-9684-beea16aa860a | -2.95336 | -51.05757 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1c9582c7-6699-3e98-a1b2-3488d830f05e | -2.95266 | -51.06216 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3ee561f4-6849-3c48-b655-f7c00e1d2740 | -2.91702 | -51.46965 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ab2768e-76c9-30cc-a988-39ef9158a7a6 | -2.91334 | -51.4691 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bdf4f0c-d126-3dc6-8a99-bfac772fa7e3 | -2.89967 | -51.4847 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5538cbce-e036-3434-b98a-1caca6d32293 | -2.88807 | -51.65775 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edd92d42-09d7-35ae-9a92-64499f5d099d | -2.88742 | -51.66197 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a60b946b-0393-3079-bf6f-6dd3c0a9618f | -2.88509 | -51.65295 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b15fcc2e-f0c0-3d3c-9d2b-919410bd7059 | -2.8849 | -51.30838 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c77f3153-bdcb-3cd5-a06b-389f2d59ee4f | -2.88444 | -51.65717 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8324206-ec04-3c3d-bd48-ccc4ff825c50 | -2.88423 | -51.31279 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 84942d91-b157-3058-b7ae-9a9ab0d1263f | -2.88379 | -51.66139 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4ab2ef0-1137-3290-9495-f9e36f6860ab | -2.88119 | -51.30781 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7c55ee6c-a38a-3207-853f-db2dac96ad0d | -2.88081 | -51.65659 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e5a8148-311c-322d-8357-3fed681308c8 | -2.88053 | -51.31221 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5929d71d-9041-3621-a4d7-6ad2eed8e77c | -2.87748 | -51.30724 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bfdaab89-0375-3af5-b5d1-c7fb80c9a535 | -2.87682 | -51.31164 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dd775a39-bff0-3353-8a3c-3cdb549a753a | -2.87616 | -51.31604 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 36c22049-fa30-3678-9d53-b44d65146b3f | -2.87573 | -51.61678 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbb35928-948d-34f9-8c96-61c172b24457 | -2.87378 | -51.30667 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| edc49f28-c74f-3e97-9d15-76885da7150b | -2.87312 | -51.31107 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ccfd5f32-7293-3545-8884-619fc85cb006 | -2.86902 | -51.07485 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9baebd20-3546-34b4-86e7-18ff345038a0 | -2.85963 | -51.28418 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edb2d8fb-22cd-350f-8098-9f12d290824a | -2.85894 | -51.28859 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb2ebbb3-b231-3d60-a333-ee95090d07be | -2.85592 | -51.28361 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 364f31ef-8290-3833-a08b-2cbbd08513d5 | -2.85524 | -51.28801 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d114725-7795-328c-ae4f-6d23b30a2eb4 | -2.85455 | -51.29243 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61bcbbf3-c2e3-3123-ba86-586662b7dca1 | -2.85414 | -51.36209 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9aa4c01-65fe-393a-a19c-54d775ffe2fc | -2.85174 | -51.35939 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8045945d-cb64-36da-87c4-eb3d2fc33451 | -2.85153 | -51.28743 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99fd69d5-b056-373e-8d4f-5e86ef994fa5 | -2.8511 | -51.35711 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77981344-a924-3574-847d-dbf4890220ee | -2.85106 | -51.36376 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 292d0bbd-8314-318c-aca3-0cd5aeb72a4a | -2.85045 | -51.36149 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30cda34b-6c65-3377-a552-bba788dea7ee | -2.82872 | -51.03636 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35b1f08d-53c6-3ca7-a449-c1be05c8f8ca | -2.81984 | -51.34555 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6725cdf2-5e33-3b45-9418-24956fb34246 | -2.81312 | -51.34003 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59f1c424-c01b-393b-8085-6f187b65dcab | -2.81245 | -51.34441 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06f9d520-5b7e-360c-8459-d1b24ad2f4d1 | -2.80943 | -51.33946 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a85c8cb8-7164-3807-b598-e902d2fbfe47 | -2.80876 | -51.34383 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9021fe4d-5c79-3778-ad5d-46736e76bdee | -2.80809 | -51.34821 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbc96784-aed2-376b-a668-ab1f7a19425e | -2.80269 | -51.60299 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc10a7bc-8c5a-3012-ab53-8985a19a7ce3 | -2.80203 | -51.60724 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad283e40-915f-31a7-97a4-ece2efdaa624 | -2.79971 | -51.59817 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a45d08-b3d3-3a98-919f-f373be2946cd | -2.79905 | -51.60244 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 38e327b2-19e1-3927-aaca-ba13703ceb1b | -2.79839 | -51.60669 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4178d561-fdcd-3ffd-91f1-273df6a3e8bf | -2.79773 | -51.61092 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 35325108-be93-30ef-ae2b-3e04be79e76d | -2.7954 | -51.60189 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 99377c3f-91e4-39d3-9335-d3447c475c9c | -2.79475 | -51.60612 | 2024-11-02 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 28c6b0c2-4d08-397c-a0bc-108c3c63ec60 | -2.7698 | -51.67147 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4242e48-21d0-328e-9fad-374dbdd3b2d7 | -2.76617 | -51.67091 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e368797-712d-30cb-8908-56c8f01e0a4a | -2.76552 | -51.67512 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b8fc730-2f03-321f-8262-a1a1dc0d65fe | -2.76254 | -51.67034 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6afb28de-ae8d-3065-a0e7-4b3983d04c3e | -4.13127 | -51.03017 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 929ba49a-0099-3457-afb8-0bdf51290500 | -4.12808 | -51.07792 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8624e0c4-ec45-3fb7-b9af-52a37bb893a7 | -4.12495 | -51.07272 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0e60084e-feee-39f1-9a15-d71980cab96f | -4.12423 | -51.07752 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 97eb117a-6284-32a6-890b-55548443fd26 | -3.99017 | -51.04019 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 906102f4-248d-392b-a618-e4b84c1116d9 | -3.98112 | -50.89978 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55a9500a-8434-30c8-82b4-55b1bb46110b | -3.91884 | -52.11714 | 2024-11-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bbe97f58-66db-3e62-bed4-33db695282ea | -3.89466 | -50.98717 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 016b8b9c-7813-3684-9c2e-9bc8ec5b1d5d | -3.89386 | -50.98432 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 534cfa59-2222-31ba-a4bf-01eef35e3625 | -3.89317 | -50.98896 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 70d4ff78-1a4a-3c49-aad0-1690b171ea3f | -3.89083 | -50.98661 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| cbbcc76a-d271-3fc3-b0a3-6f97960e0024 | -3.89011 | -50.99125 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7db6b88e-f179-3ebb-a0be-a727b0359ebb | -3.89003 | -50.98373 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9ded9345-92de-3181-8ee7-ceb39b94a17c | -3.88934 | -50.98841 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 29ff7f00-d043-375f-9975-a23af6da53b7 | -3.88866 | -50.99305 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3282cdbe-e6dc-335d-aee7-80bf31fdb5d5 | -3.88624 | -51.03603 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88e25893-2293-374b-a907-20e421e26f16 | -3.8836 | -51.03351 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README71.md)
