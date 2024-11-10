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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52912398-397f-3b3c-b140-d309525e135d | -17.60467 | -57.52172 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| d3a7a05f-777f-390a-9a37-c4c6d6a02758 | -17.60324 | -57.52942 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| addebcd2-2848-38b8-b7b5-539efadeaa76 | -17.61092 | -57.51102 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 6b6a70e6-8e0d-3eb9-878a-1b1470fb8dd2 | -17.60807 | -57.52641 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| 83ddaf71-3b3d-3acd-b0ca-5a0490d7a831 | -17.63287 | -57.50753 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 10370db0-3e75-3153-8147-540a2082ce7a | -22.53957 | -48.81403 | 2024-11-10 04:42:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6759b9de-e72f-32b7-a729-be6aad58a3a7 | -17.62665 | -57.51823 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 547b9e93-a935-343f-973f-6536bca13923 | -17.63089 | -57.49519 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| bfdc30c5-4e9f-3540-b033-5747efc8d28f | -17.61956 | -57.44131 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6e76fdce-2023-360c-97db-6536964f3e6b | -17.29177 | -57.50124 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 5f369e9d-4a3a-3f6f-8183-592a21449694 | -17.60593 | -57.53797 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 2341824f-213e-33a5-9bea-654147852109 | -17.62594 | -57.52208 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 6e590086-6fb9-3fdd-b648-e85305a36f74 | -17.23809 | -57.49032 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 87d0839f-becf-3ccf-b009-7a3c87b7a555 | -17.62197 | -57.49734 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b812f601-be34-39be-93f9-eab625fe65ce | -18.34177 | -55.59183 | 2024-11-10 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f8125429-2c89-3298-9e72-4b82e2b87666 | -17.62112 | -57.52509 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 79edf850-43a4-3873-9f4a-e55db5ffa9bd | -17.29661 | -57.49821 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 743d40db-2d2c-3a1b-a4ad-30a573a1a480 | -19.02311 | -57.62134 | 2024-11-10 04:42:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 017d99bc-1dd3-357c-9212-603e9329bd6f | -17.24222 | -57.49116 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 22d27698-894b-39d5-a3c0-3019cc5b6fc8 | -17.61645 | -57.50418 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fc53121d-b071-3b66-82f7-fbb940c99b8b | -17.30216 | -57.49129 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b91027bc-97e6-300a-a18b-9c35e7b3fce9 | -17.28692 | -57.50428 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 1592cee8-c7ac-3e4f-a03c-bb176f8cccb1 | -17.62466 | -57.50586 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e8c10c40-b6a4-3669-bcf5-35fe8dfb59ff | -17.62537 | -57.50202 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d0a8d3ee-001f-36ae-9583-81cc4955f908 | -17.62452 | -57.52978 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| f443512e-e3e3-31f9-8cae-0cc266996102 | -18.87891 | -53.05251 | 2024-11-10 04:42:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e32bba4-749e-35e6-80e1-e92bf336434e | -17.28835 | -57.49652 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| f553a5ee-7b5e-377d-a91f-a3f1a619cb70 | -17.61021 | -57.51487 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| f39b164b-c140-387e-bd19-f6e3b5ae6011 | -21.19318 | -44.93733 | 2024-11-10 04:42:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4d3adc1b-545b-33cb-bb30-a44eca9f8cbd | -22.16924 | -53.30926 | 2024-11-10 04:42:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d5b96f87-c049-3916-8e40-505ecabca194 | -17.6061 | -57.51402 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 35330863-ada6-3fdc-a349-fa3c4d71a22a | -17.24707 | -57.48812 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| af19676f-1364-3d6e-8a85-124b8fda6055 | -17.77527 | -54.9325 | 2024-11-10 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 683d2b87-08ef-37b2-b5e7-1e54d9394237 | -17.60587 | -57.44643 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f55e235b-2c68-3782-b0f7-19b4d932c05d | -17.30074 | -57.49905 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 65c487a6-1195-3d4d-b661-2ab373b0178e | -17.60396 | -57.52557 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| c5156a1a-2cd1-3129-8a79-e9fe90625e23 | -17.61432 | -57.51571 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 4f6e4cac-f232-3cdb-98cd-e5407c77afb9 | -17.62608 | -57.49818 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f987c0f9-2035-3106-92ba-b82e31398930 | -17.59556 | -57.45617 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cd13ac68-e823-3b3e-b4fa-9e520911b623 | -17.62736 | -57.51439 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 18abac93-345a-3e0b-af6c-a9e25ef7db8a | -17.63005 | -57.52292 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 0eb92019-5b3c-397f-bb91-3ad46b68c021 | -17.60539 | -57.51787 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| dc214ac6-37a4-31b3-b9c9-5cdbaf7ea593 | -17.63018 | -57.49903 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| bd663e4a-842b-313a-b064-a29eec6014dc | -17.24367 | -57.48341 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5245e6f0-d890-36bd-9fb0-99052e5c7d5e | -17.62268 | -57.4935 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 29d6ed85-42aa-37ac-ab17-b40f3eacbc7f | -18.87557 | -53.05191 | 2024-11-10 04:42:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 595525eb-05f0-3c2e-89c6-b628051b46b1 | -23.33928 | -46.77308 | 2024-11-10 04:42:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c9131fab-4573-36d3-9a9b-62836e81be43 | -17.62325 | -57.51354 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2c7c30ad-1aa6-33d7-9713-1e038e2b67b5 | -17.61985 | -57.50885 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 3559eb1b-7a48-38d0-873f-726a626fd19a | -17.61218 | -57.52726 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| f3d91e5b-38f9-342b-a50a-26eb81c00354 | -17.27938 | -57.49872 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dda217b7-d31e-352e-9ca2-633a27f6feef | -17.60878 | -57.52256 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| ec77e67d-2971-3068-a141-47665d38e0ec | -19.57177 | -54.46523 | 2024-11-10 04:42:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1722b11d-c64e-305d-a1c2-ed783f29d805 | -16.94233 | -57.6533 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 753405b9-0e3e-376f-baf5-28b565913e58 | -17.60681 | -57.51017 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| c0e85e84-f598-3c56-ab64-7634c80b494b | -17.61503 | -57.51186 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| f0d0b6bf-588a-3641-850a-3d7a38ea4f20 | -17.60736 | -57.53027 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 079a79a4-d925-3b0c-936f-e72a2fd66abc | -18.78887 | -52.58429 | 2024-11-10 04:42:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 941c7bf2-7a90-34e7-94db-62d81175da97 | -17.24149 | -57.49504 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| bdd857ff-fa11-3441-b72e-56fa69eecb66 | -20.76414 | -46.76943 | 2024-11-10 04:42:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 901fb7df-edab-3b2b-9362-02d245854491 | -17.28979 | -57.48877 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 3fd6133a-4090-36ba-aa62-635986b474e5 | -17.63076 | -57.51907 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 290c9526-4dc6-332a-8421-6e60eba4e3d6 | -17.6197 | -57.53279 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 9cd78b00-2827-332d-be69-536003eaa1f2 | -17.59913 | -57.52857 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fe654281-ed8f-3813-bf5a-49901b079f95 | -21.89983 | -57.26979 | 2024-11-10 04:42:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa086d85-3983-3b8c-be72-323558ccec5c | -17.62041 | -57.52894 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 536fcc45-bc6a-3acd-ba91-c59ef310ae61 | -17.29733 | -57.49433 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 0a60e42b-0815-3afa-8d51-1d6b674c7ada | -17.28907 | -57.49265 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| f2d7c545-96cf-362a-bb17-de05b0283606 | -17.29463 | -57.48574 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 502df4bb-3b1f-3c33-864f-84acf6b66371 | -17.68427 | -57.51829 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f143b6ea-52ba-3684-b78a-4b6d9bab5dcc | -17.2905 | -57.4849 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 882c1512-e413-3909-ab33-d096a27ef831 | -17.61361 | -57.51955 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 6b46ad59-b988-3099-a620-a0b164685b3a | -17.62749 | -57.49052 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7cd9443d-de25-3174-add5-5634c8012c12 | -17.62183 | -57.52124 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 4b1aab44-8bd0-3a45-902e-de88e4e9fcf8 | -17.77171 | -54.93184 | 2024-11-10 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 778336dd-dab2-3354-bb57-fabc646a27d8 | -17.29946 | -57.48272 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9169ccd2-fdd4-3e1d-87a3-e05555095b76 | -17.2478 | -57.48425 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0b3d79c4-c8a9-3c9a-b51e-e5d3547eb668 | -17.29391 | -57.48961 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 547f07f0-cdad-3ff0-bedd-3c135089f1a5 | -19.05688 | -52.25947 | 2024-11-10 04:42:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89104525-61f1-3cb8-b32c-db2168698ebf | -22.78261 | -43.7565 | 2024-11-10 04:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 97dc306e-1ad8-3b4b-b991-f1da94352e30 | -17.62678 | -57.49435 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 96f8b8d8-e386-3139-9b7b-d6e241eb65a8 | -17.62365 | -57.44214 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fadd3f68-2361-3bcd-aaf9-75be3ab98e08 | -17.28764 | -57.5004 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 1d2d48ca-f182-326a-a943-135e1e7b93ca | -17.61914 | -57.5127 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 7d82182f-72cf-352e-aaed-c7f70f6a3af6 | -17.2512 | -57.48896 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a003d300-1510-3bb6-be89-81000c0e3d27 | -17.62523 | -57.52593 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 79810b6e-3eeb-3f81-98a0-b84ad91fad63 | -17.62395 | -57.50969 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cb88af62-9ae3-36b5-8fc1-46bfda391455 | -18.33812 | -55.59113 | 2024-11-10 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 60682200-f85d-35df-bf30-8208e5327f83 | -17.24295 | -57.48729 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fc712c2d-2b01-3d80-865d-0b279d3f40da | -17.63146 | -57.51523 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 2a45bc81-3d23-3876-9a68-73fa7598b494 | -17.6095 | -57.51871 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 8f5e330f-c3bc-36e4-b76b-8366a6414901 | -17.28423 | -57.49568 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4eb30cc5-fa88-34d6-82b0-59260efa41b2 | -20.99497 | -51.79302 | 2024-11-10 04:42:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 38075976-b1b8-3135-9d38-a65fb840dd8b | -21.58929 | -57.16175 | 2024-11-10 04:42:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80838531-7150-308c-8696-c21f78e99aca | -17.63358 | -57.5037 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e7abdce4-3441-3d4d-923c-a4701a68c1e6 | -17.62126 | -57.50118 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d41df12b-dd75-3868-8ba5-69e6beb91a7a | -17.61772 | -57.5204 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 2e871627-0029-3145-bb49-f73c1356700b | -17.60253 | -57.53328 | 2024-11-10 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 9e1cf37a-e982-3085-86dc-53727bb86d72 | -17.25946 | -57.49064 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 45bbf676-5416-3d13-b854-12d73ac498ef | -17.24635 | -57.492 | 2024-11-10 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |


[Clique aqui para ver as próximas entradas](README118.md)
